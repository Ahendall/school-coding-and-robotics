// Importing utility header
#include "util.h"

// Function prototypes
int newCustomer(Customer customer);
int existingCustomer(Customer customer);
int orderLoop(Customer customer);

// Main function to handle Instancing and customer newcheck
int main() {
    // Creating instance of customer Class
    Customer customer(lower(getString("What is your name?\n")));

    // Checking if custoemr is new
    if (customer.isNew)
        return newCustomer(customer);

    else
        return existingCustomer(customer);
}


// Defining function prototypes
int newCustomer(Customer customer) {
    // Print welcome message and menu
    cout << "Welcome, " << customer.name << ". Since you are a new customer, here is $1000.00 to spend here \n";
    cout << "Here is our menu for today:\n\n";
    printMenu();

	return orderLoop(customer);
}


// Same as above, but adds option for customer to re-order their previous order
int existingCustomer(Customer customer) {
    cout << "Welcome back, " << customer.name << ". Your remaining balance is: $" << customer.cash << "\n";
    cout << "Here is our menu for today:\n\n";
    printMenu();

    string reOrderChoice;
    do {
        cout << "\n";
        reOrderChoice = getString("Would you like to re-order your previous order?\n(y/n): ");
    } while (reOrderChoice[0] != 'y' && reOrderChoice[0] != 'n');

    if (reOrderChoice[0] == 'y') {
        bool status = customer.order();

        if (status) {
            cout << customer.checkoutMsg();
            return 0;
        }

        customer.cart.clear();
        customer.price = 0.00;
        cout << "You do not have enough money for your previous order\n";
        cout << "Try ordering something else. \n";
    }

	return orderLoop(customer);
}


// Loop that above functions will use to allow user to order
int orderLoop(Customer customer) {
	while (true) {
        string query = lower(getString(notext));

        // Customer wants to remove an order from cart
        if (slice(query, 0, 2) == "rm") {
            int status = customer.remove(strToInt(slice(query, 3)));

            if (status == 0)
                cout << "Item " << query[3] << " removed successfully. Anything else?\n";

            else if (status == 1)
                cout << "Item " << query[3] << " is not a valid order Id. Please try again.\n";

            else
                cout << "Item " << query[3] << " is not in your cart. Please try again.\n";
        }

        // Customer wants to checkout and pay
        else if (query.find("checkout") != string::npos) {
            bool status = customer.checkout();
            if (status) {
                cout << customer.checkoutMsg() << endl;
                return 0;
            } else {
                cout << "You do not have enough money!\nTry removing a few things.";
                continue;
            }
        }

        // Customer wants to add a new order to cart
        else {
            int orderId = strToInt(query);
            bool orderStatus = customer.order(orderId);

            if (not orderStatus)
                cout << "I am not familiar with the order \"" << orderId << "\". Please try again." << endl;

            else
                excellentChoice();
        }
    }
}