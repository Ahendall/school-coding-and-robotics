menu = """
+------------------------------+-------+-----------------------------------------+
|             Item             | Price | order id (type in this number to order) |
+------------------------------+-------+-----------------------------------------+
| 2 piece chicken nugget       | $2    |                                       1 |
| 5 Piece chicken nugget       | $5    |                                       2 |
| 10 (+1) Piece chicken nugget | $10   |                                       3 |
| Small fries                  | $1.25 |                                       4 |
| Medium fries                 | $2.25 |                                       5 |
| Large fries                  | $4.20 |                                       6 |
+------------------------------+-------+-----------------------------------------+
"""

menuDict = {1: {"name": "2 peice chicken nugget", "price": 2},
            2: {"name": "5 peice chicken nugget", "price": 5},
            3: {"name": "10 (+1) peice chicken nugget", "price": 10},
            4: {"name": "small fries", "price": 1.25},
            5: {"name": "medium fries", "price": 2.25},
            6: {"name": "large fries", "price": 4.20}}

orderPrompt = """
What would you like to order?
 - To add something to your cart: Type in the order id
 - To remove an item from your cart: type in `rm [order_id]`
 - To checkout and pay: type in `checkout`
"""

excellent = ["Excellent choice. ", "Wonderful! ", "A fine selection. ", "Brilliant choice. ", "Great! "]
anythingElse = ["Anything else?", "Anything else to add to your cart?", "Any more items?", "Would you like to add anything else?", "Will that be all?"]
