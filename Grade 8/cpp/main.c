#include <stdlib.h>
#include <stdio.h>
#include "sqlite/sqlite3.h"

int main(void) {
    sqlite3 *db;
    sqlite3_stmt *stmt;
    int rc = sqlite3_open("customers.db", &db);
}