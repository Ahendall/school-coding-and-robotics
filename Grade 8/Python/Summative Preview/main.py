from cs50 import SQL
from random import randint

import menu as m
from helpers import customer, get_int

# Sqlite init
db = SQL("sqlite:///customers.db")


def main():
    # Instancing class `customer`
    Customer = customer(input("What is your name?\n").lower())
    
    if Customer.isNew == True:
        # Customer is new, order_prev is disabled and different prompt
        print(f"Welcome, {Customer.name}. Since you are a new Customer, here is $1000.00 to spend here.\nHere is our menu for today:")
        print(m.menu)
        print(m.orderPrompt)

        # Getting order
        while True:
            query = input().lower()

            if query[0:2] == "rm":
                Customer.rm(int(query[3]))
                continue
            elif "checkout" in query:
                Customer.checkout()
                return

            # Checking if order is valid. If yes, running order()
            if int(query) in m.menuDict.keys():
               Customer.order(int(query))
               continue
            else:
                print(f"I am not familiar with the order \"{query}\"\n Please order again.")
                continue

    else:
        # Customer already exists in db
        # order_prev now enabled
        print(f"Welcome back, {Customer.name}. Your current balance is ${Customer.cash}\nHere is our menu for today:")
        print(m.menu)

        # Checking if customer wants re-order or new order
        re_order = get_int("To re-order your previous order, type 1.\nIf you would like to make a new order, type 2.")
        if re_order == 1:
            Customer.order(Customer.prev_order)
            return

        print(m.orderPrompt)

        # Getting order
        while True:
            query = input().lower()

            # If User wants to remove or checkout
            if query[0:2] == "rm":
                Customer.rm(int(query[3]))
                continue
            elif "checkout" in query:
                Customer.checkout()
                return

            # Checking if order is valid. If yes, running order()
            if int(query) in m.menuDict.keys():
               Customer.order(int(query))
               continue
            else:
                print(f"I am not familiar with the order \"{query}\"\n Please order again.")
                continue
        


if __name__ == "__main__":
    main()
