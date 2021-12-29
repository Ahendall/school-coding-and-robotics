from cs50 import SQL
from random import randint
from menu import *

# Sqlite init
db = SQL("sqlite:///customers.db")

# Creation of class "Customer", containing the customer's userData, cart, and nececary functions
# This is my first time using OOP, and i'm not sure if I'm doing it right buy hey it works ¯\_(ツ)_/¯ 
class customer:
    def __init__(self, name): # init instance vars
        userData = db.execute("SELECT * FROM customers WHERE name = ?", name)

        if len(userData) == 0:
            # Add user to database, set self variables
            db.execute("INSERT INTO customers (name, prev_order, prev_price) VALUES (?, '0', 0)", name)
            self.name = name
            self.cash = 1000.00
            self.prev_order = {'0': 0}
            self.cart = list()
            self.price = 0
            self.isNew = True
        else:
            # using userData to get existing user, setting self vars
            self.name = name
            self.cash = float(userData[0]["cash"])
            self.prev_order = {"prev_order": userData[0]["prev_order"], "prev_price": float(userData[0]["prev_price"])}
            self.cart = list()
            self.price = 0
            self.isNew = False

    
    def order(self, order):
        if type(order) == dict:
            # Converting previous order to list
            # O(n) because going through each element once
            prev_order = order["prev_order"]
            for i in range(len(prev_order)):
                self.cart.append(int(prev_order[i]))
            self.price = order["prev_price"]

            return self.checkout()
            pass

        else:
            # Adding value to end of cart, updating price, printing random message
            # O(1) Amortized (Since there is a chance for re-allocation of the array)
            orderInMenu = menuDict[order]
            self.price += orderInMenu["price"]
            self.cart.append(order)
            p1 = excellent[randint(0, 4)]
            p2 = anythingElse[randint(0, 4)]
            print(f"{p1}{p2}")
            return


    def rm(self, order):
        # Removing order from user's cart, updating price
        # O(n) since remove() needs to go through each element in array
        try:
            self.cart.remove(order)
            orderInMenu = menuDict[order]
            self.price -= orderInMenu["price"]
            print("Order successfully removed. Anything else?")
            return
        except:
            print(f"Item {order} does not exist in your cart.")
            print("Anything else?")
            return


    def checkout(self):
        # Convert list to str, and create message
        # Will take O(n) time bcos iterating through each element in array once
        orderStr = ""
        orderMsg = "You ordered: \n"
        for i in range(len(self.cart)):
            orderInMenu = menuDict[self.cart[i]]
            orderStr += str(self.cart[i])
            orderMsg += f" - {orderInMenu['name']}\n"

        #update usercash
        self.cash -= self.price

        # updating customers.db
        db.execute("UPDATE customers SET cash = ?, prev_order = ?, prev_price = ? WHERE name = ?", self.cash, orderStr, self.price, self.name)

        # Printing messages and returning
        print(orderMsg, end="")
        print(f"Remaining cash: ${self.cash}")
        print("Thank you for your purchase! Come again soon!")
        return

    


def get_int(prompt):
    # Loops prompting user for `prompt` until valid integer is given
    while True:
        print(prompt)
        query = input()
        try:
            query = int(query)
            break
        except:
            # Error with typecasting str to int meaning input is invalid
            continue

    return query
