#include "../Utility/util.h"
#include <cctype>
#include <iostream>
#include <map>
#include <random>
#include <sqlite3.h>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <array>

class Customer {
private:
	// Important structures
	// Struct for recieving customer info from db
	struct CustomerData {
		std::string name;
		float cash;
		std::string prev_order;
		float prev_price;

		CustomerData(std::string name, float cash, std::string prev_order, float prev_price) : name(name), cash(cash), prev_order(prev_order), prev_price(prev_price) {}
	};

	// Struct for Previous Orders
	struct PrevOrder {
		std::string order;
		float price;
	};

	// Struct for menu items
	struct MenuItem {
		std::string name;
		float price;

		MenuItem(std::string itemName, float itemPrice) {
			name = itemName;
			price = itemPrice;
		}
	};

	// Sql Members
	sqlite3 *db;
	int rc;

	// Menu Items
	std::vector<MenuItem> menu;

public:
	// std::String-based members
	std::string name;
	PrevOrder prevOrder;

	// Numeric members
	float cash;
	float price;
	std::vector<int> cart;

	// Boolean Members
	bool isNew;

	// Method Prototypes
	Customer(std::string customerName);
	bool order(int order);
	bool order();
	int remove(int order);
	int checkout();
	std::string checkoutMsg();
};