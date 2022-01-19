// Library Imports
#include <sqlite_modern_cpp.h>

#include <cctype>
#include <iostream>
#include <map>
#include <random>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

// Macros
#define MENU_ITR map<int, MenuItem>::iterator
#define notext ""

// Namespace and class uses
using namespace sqlite;
using std::array;
using std::cin;
using std::cout;
using std::endl;
using std::exception;
using std::find;
using std::getline;
using std::map;
using std::next;
using std::numeric_limits;
using std::pair;
using std::streamsize;
using std::string;
using std::stringstream;
using std::to_string;
using std::vector;

// non-class function prototypes
int getInt(string query);
string getString(string query);
string lower(string word);
void printMenu();
string slice(string str, int start, int end);
string slice(string str, int start);
int strToInt(string str);
int charToInt(char ch);
int randomInt();
void excellentChoice();
bool removeFromVector(vector<int> &arr, int target);
string checkoutMsg(vector<int> &cart);

// SQLite Init
database db("customers.db");

// Struct for recieving SQL data
struct CustomerData {
    string prev_order;
    float cash;
    float prev_price;
};

// Struct for Previous Orders
struct PrevOrder {
    string order;
    float price;
};

// Struct for menu items
struct MenuItem {
    string name;
    float price;

    MenuItem(string itemName, float itemPrice) {
        name = itemName;
        price = itemPrice;
    }
};

// Declaration of menu items + Hashmap of MenuItems
map<int, MenuItem> menu = {{1, MenuItem("2 Peice chicken nugget", 2.00)},
                           {2, MenuItem("5 Peice chicken nugget", 5.00)},
                           {3, MenuItem("10 (+1) Peice chicken nugget", 10)},
                           {4, MenuItem("Small fries", 1.25)},
                           {5, MenuItem("Medium fries", 2.25)},
                           {6, MenuItem("Large fries", 4.20)}};

// Class for active customer
class Customer {
public:
    // String-based members
    string name;
    PrevOrder prevOrder;

    // Numeric members
    float cash;
    float price = 0;
    vector<int> cart;

    // Boolean Members
    bool isNew;

    Customer(string customerName) {
        vector<CustomerData> people;
        try {
            db << "SELECT cash, prev_order, prev_price FROM customers WHERE name = ?;"
               << customerName >>
                [&](float cash, string prev_order, float prev_price) {
                    CustomerData tempCustomer;
                    tempCustomer.prev_order = prev_order;
                    tempCustomer.cash = cash;
                    tempCustomer.prev_price = prev_price;

                    people.push_back(tempCustomer);
                };
        }

        catch (exception &e) {
            cout << e.what() << endl;
        }

        if (people.size() == 0) {
            // No existing customer with name "customerName"
            db << "INSERT INTO customers (name) VALUES (?);" << customerName;
            name = customerName;
            cash = 1000.00;
            isNew = true;

            prevOrder.order = "0";
            prevOrder.price = 0.00;
        } else {
            // Existing customer found, load data into memory
            name = customerName;
            cash = people[0].cash;
            isNew = false;

            prevOrder.order = people[0].prev_order;
            prevOrder.price = people[0].prev_price;
        }
    }

    // Function that will add item "order" to user's cart. Only works with new
    // orders
    bool order(int order);

    // Function that will re-order user's previous order from previous session
    bool order();

    // Function that will remove an order from the user's cart
    int remove(int order);

    // Function that will check out the user, deduct money, and update database.
    bool checkout();

    // Function that returns an organised message of items in the cart, as well as
    // the total price of items
    string checkoutMsg();
};

// Add item order
bool Customer::order(int order) {
    // Getting iterator for order in menu
    MENU_ITR orderInMenu = menu.find(order);

    // Iterator could not find order in menu
    if (orderInMenu == menu.end())
        return false;

    cart.push_back(order);
    price += orderInMenu->second.price;
    return true;
}

// Prev Order Order
bool Customer::order() {
    price = prevOrder.price;

    // Converting prevOrder str to vector
    for (int i = 0; i < prevOrder.order.size(); i++)
        cart.push_back(charToInt(prevOrder.order[i]));

    return checkout();
}

// Remove order
int Customer::remove(int order) {
    // Menu Iteratorx
    MENU_ITR orderInMenu = menu.find(order);

    // order is invalid
    if (orderInMenu == menu.end())
        return 1;

    // Getting iterator for removal
    bool removalStatus = removeFromVector(cart, order);

    // Order is not in user's cart
    if (!removalStatus)
        return 2;

    price -= orderInMenu->second.price;
    return 0;
}

// Checkout user
bool Customer::checkout() {
    float temp = cash;
    cash -= price;

    // User does not have enough cash
    if (cash < 0) {
        cash = temp;
        return false;
    }

    // Converting cart to string (for db)
    string orderStr = "";
    for (int i = 0; i < cart.size(); i++) {
        orderStr += to_string(cart[i]);
    }

    // Updating DB
    db << "UPDATE customers SET cash = ?, prev_order = ?, prev_price = ? WHERE "
          "name = ?"
       << cash << orderStr << price << name;
    return true;
}

// Function that returns an organised message of items in the cart, as well as
// the total price of items
string Customer::checkoutMsg() {
    stringstream msg;
    map<string, int> cartMap;

    // Converting cart vector to map
    for (int i = 0; i < cart.size(); i++) {
        MENU_ITR orderInMenu = menu.find(cart[i]);
        map<string, int>::iterator it = cartMap.find(orderInMenu->second.name);

        // Checking if order is already present in map
        if (it == cartMap.end()) {
            cartMap.insert(pair<string, int>(orderInMenu->second.name, 1));
        } else {
            it->second++;
        }
    }

    // Converting map to string
    for (map<string, int>::iterator it = cartMap.begin(); it != cartMap.end();
         it++) {
        msg << " - " << it->first;

        if (it->second > 1) {
            msg << " (x" << it->second << ")";
        }

        msg << "\n";
    }

    // Adding final messages and returning stream in form of std::string
    msg << "\n"
        << "You spent: " << price << "\n"
        << "Remaining cash: $" << cash << "\n"
        << "Thank you for your purchase! Come again soon!";

    return msg.str();
}

/****************** Other Helper Functs ******************/
// Function prompting user for "query" until valid integer is given
int getInt(string query) {
    while (true) {
        int x;
        cout << query;
        cin >> x;

        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }

        return x;
    }
}

// Wrapper function for getline()
string getString(string query) {
    string x;

    // Making sure input stream is clear
    cin.clear();

    // Getting input from user
    cout << query;
    getline(cin, x);

    return x;
}

// Function that converts a string to all lowercase
string lower(string word) {
    for (int i = 0; i < word.size(); i++) {
        word[i] = tolower(word[i]);
    }

    return word;
}

// Function that will print menu and welcome message
void printMenu() {
    stringstream ss1;
    ss1 << "+------------------------------+-------+-----------------------------"
           "------------+\n";
    ss1 << "|             Item             | Price | order id (type in this "
           "number to order) |\n";
    ss1 << "+------------------------------+-------+-----------------------------"
           "------------+\n";
    ss1 << "| 2 piece chicken nugget       | $2    |                             "
           "          1 |\n";
    ss1 << "| 5 Piece chicken nugget       | $5    |                             "
           "          2 |\n";
    ss1 << "| 10 (+1) Piece chicken nugget | $10   |                             "
           "          3 |\n";
    ss1 << "| Small fries                  | $1.25 |                             "
           "          4 |\n";
    ss1 << "| Medium fries                 | $2.25 |                             "
           "          5 |\n";
    ss1 << "| Large fries                  | $4.20 |                             "
           "          6 |\n";
    ss1 << "+------------------------------+-------+-----------------------------"
           "------------+\n\n";
    ss1 << "What would you like to order?\n";
    ss1 << "- To add something to your cart: Type in the order id\n";
    ss1 << "- To remove an item from your cart: type in `rm [order_id]`\n";
    ss1 << "- To checkout and pay: type in `checkout`\n";
    cout << ss1.str();
}

// Function that implements abstract languages' "string slicing"
// Will return all characters from str[start] to str[end] (exclusive)
string slice(string str, int start, int end) {
    string slicedStr = notext;
    for (int i = start; i < end; i++) {
        slicedStr += str[i];
    }

    return slicedStr;
}

// Will return all characters from str[start] to end of str
string slice(string str, int start) {
    string slicedStr = notext;
    for (int i = start; i < str.length(); i++) {
        slicedStr += str[i];
    }

    return slicedStr;
}

// Function that converts a string to an integer using the string stream
// This typecast method is more effective than standard conversion because
// typecasting an integer in a string will return it's ascii value, not it's
// actual value
int strToInt(string str) {
    stringstream convert(str);
    int x = 0;
    convert >> x;
    return x;
}

// Function that converts a char to an int, accounting for ascii value
int charToInt(char ch) { return int(ch) - 48; }

// Helper function for excellentChoice
int randomInt() {
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist6(
        0, 4); // distribution in range [0, 4]

    return dist6(rng);
}

// Function that prints a random message based on a random int value
void excellentChoice() {
    cout << "\n";

    // Arrays of similar statements so that it's not the same every time.
    array<string, 5> excellent = {"Excellent choice. ", "Wonderful! ",
                                  "A fine selection. ", "Brilliant choice. ",
                                  "Great! "};
    array<string, 5> anythingElse = {
        "Anything else?", "Anything else to add to your cart?", "Any more items?",
        "Would you like to add anything else?", "Will that be all?"};

    // Printing the message
    cout << excellent[randomInt()] << anythingElse[randomInt()] << endl;
}

// Function that will remove an item from the cart (an integer resizable array
// (vector))
bool removeFromVector(vector<int> &arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            arr.erase(next(arr.begin(), i));
            return true;
        }
    }

    return false;
}