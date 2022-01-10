#include <map>
#include <vector>
#include <iostream>
#include "sqlite/sqlite3.h"

using std::string;
using std::vector;
using std::endl;
using std::cout;
using std::fixed;
using std::map;

class Customer {
    public:
    // Attribute Declaration
    string name;
    string cash;
    string prevOrder;
    float prevPrice;
    vector<int> cart;
    float price;
    bool isNew;

    // SQLite init

    // Constructor
    Customer(string n) {

    }
};