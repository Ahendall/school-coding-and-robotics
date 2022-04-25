#include <iostream>
#include <sqlite3.h>
using namespace std;

int main(int argc, char **argv) {
    sqlite3 *db;

    // Create database connection
    int rc = sqlite3_open("customers.db", &db);
    if (rc) {
        cout << "Can't open database: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return 1;
    }

    // get data from table "customers" and print it out
    string sql = "SELECT * FROM customers";
    sqlite3_stmt *stmt;
    rc = sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, NULL);
    if (rc != SQLITE_OK) {
        cout << "Preparation failed: " << sqlite3_errmsg(db) << endl;
        sqlite3_close(db);
        return 1;
    }

    // print out data
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        cout << "Customer Name: " << sqlite3_column_text(stmt, 0) << endl;
        cout << "Cash: " << sqlite3_column_text(stmt, 1) << endl;
        cout << "prev_order: " << sqlite3_column_double(stmt, 2) << endl;
        cout << "prev_price: " << sqlite3_column_int(stmt, 3) << endl;
    }
}