from cs50 import SQL

class Customer:
    # Inner Classes
    class MenuItem:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __str__(self):
            return f"{self.name} - ${self.price}"

    # Class members
    _db = SQL("sqlite:///customers.db")
    menuItems = [
        MenuItem("2 Piece Chicken Nugget", 2.99),
        MenuItem("5 Piece Chicken Nugget", 5.99),
        MenuItem("10 (+1) Piece Chicken Nugget", 10.99),
        MenuItem("Golden Burger", 69.42),
        MenuItem("Small Fries", 1.25),
        MenuItem("Medium Fries", 2.25),
        MenuItem("Large Fries", 4.20),
        MenuItem("Waffle", 3.99),
        MenuItem("Cookie", 1.99),
        MenuItem("Ice Cream", 2.99),
        MenuItem("Fountain Drink", 1.00),
        MenuItem("Bottle of Water", 1.00),
    ]

    def __init__(self, name):
        userData = self._db.execute(
            "SELECT * FROM customers WHERE name = ?",
            name
        )

        if userData:  # Customer already exists in db
            # Set instance members
            self.name = name
            self.cash = float(userData[0]["cash"])
            self.prev_order = userData[0]["prev_order"]
            self.prev_price = float(userData[0]["prev_price"])
            self.cart = list[int]
            self.price = 0
            self.isNew = False
        else:
            self._db.execute(
                "INSERT INTO customers (name, prev_order, prev_price) VALUES (?, '0', 0)",
                name
            )  # Adding user to database

            # Set instance members
            self.name = name
            self.cash = 1000.00
            self.prev_order = "0"
            self.prev_price = 0
            self.cart = list[int]
            self.price = 0
            self.isNew = True

    def order(self, order: int) -> int:
        # Make sure order is valid
        order -= 1  # Subtract 1 to make it 0-indexed
        if (order < 0) or (order > 11):
            return -1

        # Add order to cart
        self.cart.append(order)
        self.price += self.menuItems[order].price
        return 0

    def order(self) -> int: # Function orders previous order instead of new order
        # convert order from csv to list of ints
        order = self.prev_order.split(",")
        for item in order:
            self.cart.append(int(item))
        self.price = float(self.prev_price)
        return self.checkout()

    def rm(self, order: int) -> int:
        # Make sure order is valid
        order -= 1
        if (order < 0) or (order > 11):
            return -1

        # Remove order from cart
        if order not in self.cart:
            return -2
        self.cart.remove(order)
        return 0

    def checkout(self) -> bool:
        # Make sure user has enough cash
        if self.price > self.cash:
            return False
        self.cash -= self.price

        # Convert cart to csv str
        order = ""
        for item in self.cart:
            order += str(item) + ","
        order = order[:-1] # Remove trailing comma

        # Update DB
        self._db.execute(
            "UPDATE customers SET cash = ?, prev_order = ?, prev_price = ? WHERE name = ?",
            self.cash,
            order,
            self.price,
            self.name
        )

        return True

    def getReciept(self) -> str:
        reciept = {}
        for item in self.cart:
            if item in reciept.keys():
                reciept[item] += 1
            else:
                reciept[item] = 1
        recieptStr = "\033[2;32mYou ordered:\033[0m\n\n"
        for item, quantity in reciept.items():
            recieptStr += f" - {self.menuItems[item].name} (x{quantity})\n"
        recieptStr += f"\n\033[2;32mTotal: ${self.price} \nRemaining cash: ${self.cash}\n[0m"
        recieptStr += "Have a good day!"
        return recieptStr