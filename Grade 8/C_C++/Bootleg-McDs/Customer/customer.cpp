#include "customer.h"
using std::array, std::exception, std::map, std::numeric_limits, std::pair, std::streamsize, std::string, std::stringstream, std::vector;
using std::endl, std::find, std::getline, std::next, std::to_string, std::cin, std::cout, std::stoi;

// Constructor
Customer::Customer(string customerName) {
	// Initialize sqlite3
	stringstream ss;
	rc = sqlite3_open("customers.db", &db);
	if (rc) {
		cout << "Can't open database: " << sqlite3_errmsg(db) << "\n";
		sqlite3_close(db);
		return;
	}

	// Statement prep
	ss << "SELECT cash, prev_order, prev_price FROM customers WHERE name = '" << antiSqlInjection(customerName) << "';";
	string sql = ss.str();
	sqlite3_stmt *stmt;
	rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
	if (rc != SQLITE_OK) {
		cout << "Preparation failed: " << sqlite3_errmsg(db) << "\n";
		sqlite3_close(db);
		return;
	}

	// Load data into vector of people
	vector<CustomerData> people;
	while (sqlite3_step(stmt) == SQLITE_ROW) {
		people.push_back(
			CustomerData(
				customerName,
				sqlite3_column_double(stmt, 1),
				string(reinterpret_cast<const char *>(sqlite3_column_text(stmt, 2))),
				sqlite3_column_double(stmt, 3)));
	}

	if (people.size() == 0) {
		isNew = true;
		name = customerName;
		cash = 0;
		prevOrder.order = "1";
		prevOrder.price = 0;
		price = 0;

		// insert new customer into db
		ss.str("");
		ss << "INSERT INTO customers (name) VALUES ('" << antiSqlInjection(name) << "');";
		sql = ss.str();
		rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
		if (rc != SQLITE_OK) {
			cout << "Preparation failed: " << sqlite3_errmsg(db) << "\n";
			sqlite3_close(db);
			return;
		}
	} else {
		price = 0;
		isNew = false;
		name = customerName;
		cash = people[0].cash;
		prevOrder.order = people[0].prev_order;
		prevOrder.price = people[0].prev_price;
	}

	menu = {
		MenuItem("2 Piece chicken nuggets", 2.99),
		MenuItem("5 Piece chicken nuggets", 4.99),
		MenuItem("10 (+1) Piece chicken nuggets", 6.99),
		MenuItem("2 Piece chicken wings", 3.99),
		MenuItem("5 Piece chicken wings", 5.99),
		MenuItem("10 (+1) Piece chicken wings", 7.99),
		MenuItem("Small fries", 0.99),
		MenuItem("Medium fries", 1.99),
		MenuItem("Large fries", 2.99),
		MenuItem("Fountain soft drink", 0.99),
		MenuItem("Bottled water", 0.99),
		MenuItem("Lemonade", 1.99),
	};
}

// Ordering functions
bool Customer::order(int order) {
	// Check if order is valid
	order -= 1;
	if (order < 0 || order > 11) return false;

	cart.push_back(order);
	price += menu[order].price;
	return true;
}

bool Customer::order() {
	// convert prev_order from csv to vector<int>
	stringstream ss(prevOrder.order);
	string item;
	while (getline(ss, item, ',')) {
		cart.push_back(stoi(item));
	}

	price = prevOrder.price;
	return checkout();
}

int Customer::remove(int order) {
	// Check if order is valid
	order -= 1;
	if (order < 0 || order > 11) return 1;

	// Check if order is in cart
	vector<int>::iterator it = find(cart.begin(), cart.end(), order);
	if (it == cart.end()) return 2;

	// Remove order from cart
	cart.erase(it);

	// Update price
	price -= menu[order].price;
	return 0;
}

int Customer::checkout() {
	// Check if cart is empty
	if (cart.size() == 0) return 1;

	// Check if customer has enough cash
	if (price > cash) return 2;

	// Convert cart to csv string for db
	stringstream ss;
	for (int i = 0; i < cart.size(); i++) {
		ss << cart[i] << ",";
	}
	string order = ss.str();
	order.pop_back();

	// Update customer's cash
	cash -= price;

	// Update db
	stringstream ss2;
	ss2 << "UPDATE customers SET cash = " << cash << ", prev_order = '" << order << "', prev_price = " << price << " WHERE name = '" << name << "';";
	string sql = ss2.str();
	sqlite3_stmt *stmt;
	rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
	if (rc != SQLITE_OK) {
		cout << "Preparation failed: " << sqlite3_errmsg(db) << "\n";
		sqlite3_close(db);
		return 3;
	}

	cout << checkoutMsg() << "\n";
	return true;
}

string Customer::checkoutMsg() {
	stringstream ss;
	map<string, int> cartMap;

	// Converting cart vector to map
	for (int i = 0; i < cart.size(); i++) {
		auto orderInMenu = menu[cart[i]];
		map<string, int>::iterator it = cartMap.find(orderInMenu.name);

		// Checking if order is already present in map
		if (it == cartMap.end()) {
			cartMap.insert(pair<string, int>(orderInMenu.name, 1));
		} else {
			it->second++;
		}
	}
	// Converting map to string
	ss << "\nYou Ordered:\n";
	for (map<string, int>::iterator it = cartMap.begin(); it != cartMap.end(); it++) {
		ss << " - " << it->first;

		if (it->second > 1) {
			ss << " (x" << it->second << ")";
		}

		ss << "\n";
	}

	// Adding final messages and returning stream in form of std::string
	ss << "\n"
	   << "You spent: $" << price << "\n"
	   << "Remaining cash: $" << cash << "\n"
	   << "Thank you for your purchase! Come again soon!";

	return ss.str();
}