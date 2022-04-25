// Importing utility header
#include "Customer/customer.h"
#include "Utility/util.h"

// Function prototypes
int newCustomer(Customer customer);
int existingCustomer(Customer customer);
int orderLoop(Customer customer);

// Main function to handle Instancing and customer newcheck
int main() {
	// Creating instance of customer Class
	Customer customer(
		lower(
			getString("What is your name?\n")));

	// Checking if customer is new
	if (customer.isNew)
		return newCustomer(customer);

	else
		return existingCustomer(customer);
}

// Defining function prototypes
int newCustomer(Customer customer) {
	// Print welcome message and menu
	std::cout << "Welcome, " << customer.name << ". Since you are a new customer, here is $1000.00 to spend here \n";
	std::cout << "Here is our menu for today:\n\n";
	printMenu();

	return orderLoop(customer);
}

// Same as above, but adds option for customer to re-order their previous order
int existingCustomer(Customer customer) {
	std::cout << "Welcome back, " << customer.name << ". Your remaining balance is: $" << customer.cash << "\n";
	std::cout << "Here is our menu for today:\n\n";
	printMenu();

	std::string reOrderChoice;
	do {
		std::cout << "\n";
		reOrderChoice = getString("Would you like to re-order your previous order?\n(y/n): ");
	} while (reOrderChoice[0] != 'y' && reOrderChoice[0] != 'n');

	if (reOrderChoice[0] == 'y') {
		bool status = customer.order();

		if (status) {
			std::cout << customer.checkoutMsg();
			return 0;
		}

		customer.cart.clear();
		customer.price = 0.00;
		std::cout << "You do not have enough money for your previous order\n";
		std::cout << "Try ordering something else. \n";
	}

	return orderLoop(customer);
}

// Loop that above functions will use to allow user to order
int orderLoop(Customer customer) {
	while (true) {
		std::string query = lower(getString(notext));

		// Customer wants to remove an order from cart
		if (slice(query, 0, 2) == "rm") {
			int status = customer.remove(std::stoi(slice(query, 3)));

			if (status == 0)
				std::cout << "\nItem " << query[3] << " removed successfully. Anything else?\n";

			else if (status == 1)
				std::cout << "\nItem " << query[3] << " is not a valid order Id. Please try again.\n";

			else
				std::cout << "\nItem " << query[3] << " is not in your cart. Please try again.\n";
		}

		// Customer wants to checkout and pay
		else if (query.find("checkout") != std::string::npos) {
			bool status = customer.checkout();
			if (status) {
				std::cout << customer.checkoutMsg() << "\n";
				return 0;
			} else {
				std::cout << "\nYou do not have enough money!\nTry removing a few things.\n";
				continue;
			}
		}

		// Customer wants to add a new order to cart
		else {
			int orderId = std::stoi(query);
			bool orderStatus = customer.order(orderId);

			if (not orderStatus)
				std::cout << "\nI am not familiar with the order \"" << query << "\". Please try again."
						  << "\n";

			else
				excellentChoice();
		}
	}
}
