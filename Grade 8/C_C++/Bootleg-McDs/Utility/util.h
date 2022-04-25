// Library Imports
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cctype>
#include <sqlite3.h>
#include <sstream>
#include <utility>
#include <random>

// Macros
#define notext ""

// non-class function prototypes
int getInt(std::string prompt);
int randomInt(int start, int end);

std::string getString(std::string query);
std::string lower(std::string word);
std::string slice(std::string str, int start, int end);
std::string slice(std::string str, int start);
std::string antiSqlInjection(std::string query);

void excellentChoice();
void printMenu();