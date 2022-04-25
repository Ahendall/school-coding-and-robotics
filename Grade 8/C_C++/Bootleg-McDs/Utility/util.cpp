#include "util.h"
using std::exception, std::map, std::numeric_limits, std::pair, std::streamsize, std::string, std::stringstream, std::vector;
using std::endl, std::find, std::getline, std::next, std::to_string, std::cin, std::cout;

// Wrapper for cin that only allows for integers
int getInt(string query) {
	while (true) {
		int x;
		cout << query;
		cin >> x;

		if (cin.fail()) {
			// Saftey measures to insure that cin doesn't bug out
			// And infinitely continue the loop
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			continue;
		}

		return x;
	}
}

// Wrapper for random_device
// https://stackoverflow.com/a/13445752/10853009
int randomInt(int start, int end) {
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_int_distribution<std::mt19937::result_type> dist6(start, end); // distribution in range [start, end]

	return dist6(rng);
}

// Wrapper for cin
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
	for (auto &x : word) {
		x = tolower(x);
	}
	return word;
}

// Function that implements abstract languages' "string slicing"
string slice(string str, int start, int end) {
	stringstream ss;
	for (int i = start; i < end; i++) {
		ss << str[i];
	}
	return ss.str();
}

string slice(string str, int start) {
	return slice(str, start, str.size());
}

string antiSqlInjection(string query) {
	// Replacing all single quotes with two single quotes
	for (int i = 0; i < query.size(); i++) {
		if (query[i] == '\'') {
			query.replace(i, 1, "''");
			i++;
		}
	}

	return query;
	// Yes this method is dogshit but
    // i have no idea how to use parameters using the standard sqlite library
}

void excellentChoice() {
	cout << "\n";

	// make Arrays of similar statements so that we get variation in the statements
    vector<string> excellent = {
        "Excellent choice. ",
        "Wonderful! ",
        "A fine selection. ",
        "Brilliant choice. ",
    };
	
    vector<string> anythingElse = {
        "Anything else?",
        "Anything else to add to your cart?",
        "Any more items to add?",
        "Would you like to add anything else?",
        "Will that be all?",
    };

	// Printing the message
	cout << excellent[randomInt(0, 4)] << anythingElse[randomInt(0, 4)] << endl;
}

void printMenu() {
    cout << "0";
}