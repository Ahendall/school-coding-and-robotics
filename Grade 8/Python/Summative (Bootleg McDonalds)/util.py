from random import choice
import os
from typing import OrderedDict

def getInt(prompt: str) -> int:
	# Loops prompting user for `prompt` until valid integer is given
	while True:
		print(prompt)
		query = input()
		try:
			query = int(query)
			break
		except ValueError:
			# Error with typecasting str to int meaning input is invalid
			continue

	return query

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def clearLines(cart, itemToPrint):
	# make sure cart has no duplicates
	uniqueCart = list(OrderedDict.fromkeys(cart))
	print(itemToPrint, end="")
	for i in range(len(uniqueCart) + 4):
		print("\033[F\033[K", end="")

def clearSetLines(lineCount: int):
	for i in range(lineCount):
		print("\033[F\033[K", end="")

def getMenu() -> str:
	return"""+----+------------------------------+-------------+
| Id |             Item             | Price (USD) |
+----+------------------------------+-------------+
|  1 | 2 Piece Chicken Nugget       |       $2.99 |
|  2 | 5 Piece Chicken Nugget       |       $5.99 |
|  3 | 10 (+1) Piece Chicken Nugget |      $10.99 |
|  4 | Golden Burger                |      $69.42 |
|  5 | Small Fries                  |       $1.25 |
|  6 | Medium Fries                 |       $2.25 |
|  7 | Large Fries                  |       $4.20 |
|  8 | Waffle                       |       $3.99 |
|  9 | Cookie                       |       $1.99 |
| 10 | Ice Cream                    |       $2.99 |
| 11 | Fountain Drink               |       $1.00 |
| 12 | Bottle of Water              |       $1.00 |
+----+------------------------------+-------------+"""


def getOrderPrompt() -> str:
	return """What would you like to order?
	- To add something to your cart: Type in the order id
	- To remove an item from your cart: type in `rm [order_id]`
	- To checkout and pay: type in `checkout`

You ordered:


What would you like to order? """


def getExcellentChoiceMsg() -> str:
	excellent = ["Excellent choice. ",
				 "Wonderful! ",
				 "A fine selection. ",
				 "Brilliant choice. ",
				 "Great! "]

	anythingElse = ["Anything else?",
					"Anything else to add to your cart?",
					"Any more items?",
					"Would you like to add anything else?",
					"Will that be all?"]

	return f"{choice(excellent)}{choice(anythingElse)}"
