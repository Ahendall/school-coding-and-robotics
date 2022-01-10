#include "sqlite/sqlite3.h"
#include "util.h"
#include <iostream>
#include <map>
#include <vector>

int main(void) {
  sqlite3 *db;
  sqlite3_stmt *stmt;
  int rc;
  rc = sqlite3_open("customers.db", &db);
}
