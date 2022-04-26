"""
Functions in this file will not have a specified return type
since they will exit through sys.exit()
"""

import util
import Customer
import os
import sys
from termcolor import colored, cprint

def main():
	util.clearScreen()
	customer = Customer.Customer(
		input("What is your name?\n").lower()
	)

	util.clearScreen()
	if customer.isNew:
		return newCustomer(customer)
	else:
		return returningCustomer(customer)

def returningCustomer(customer: Customer.Customer):
	print("Welcome back to Bootleg McDonalds, " + colored(customer.name, 'cyan') + "!")
	orderChoice = util.getInt("To re-order your previous order, type in 1. To make a new order, type in any other number.")
	if orderChoice == 1:
		orderStatus = customer.orderPrev()
		if orderStatus == 0:
			print(customer.getReciept())
			sys.exit(0)
		else:
			err = colored("You do not have enough money! Please make a new order instead.", 'red', attrs=['bold'])
			customer.cart = []
			customer.price = 0
			return orderLoop(customer, [err, "Here is our menu for today:"])

	return orderLoop(customer, [])

def newCustomer(customer: Customer.Customer):
	args = ["Welcome to Bootleg McDonalds, " + colored(customer.name, 'cyan') + "!",
			"Since you are a new customer, here is " + colored('$1,000', 'green') + " to spend here with us.",
			"Here is our menu for today:"]
	return orderLoop(customer, args)

def orderLoop(customer: Customer.Customer, args: list):
	util.clearScreen()
	for arg in args:
		print(arg)
	print()

	# Print out the menu
	cprint(util.getMenu(), 'cyan', attrs=['bold'])
	print(util.getOrderPrompt())

	while True:
		order = input(colored("order >> ", 'cyan'))

		if order.lower().startswith("rm"):
			try:
				order = int(order[3:])
				orderStatus = customer.rm(order)
				if orderStatus == -1:
					cprint("Invalid order number! Try again.", 'red')
				elif orderStatus == -2:
					cprint("Order not in cart! Try again.", 'red')
				util.clearLines(customer.cart, customer.itemToPrint)
				print(customer.getCart())
				cprint(util.getExcellentChoiceMsg(), 'green', attrs=['bold'])
				continue
			except ValueError:
				util.clearLines(customer.cart, customer.itemToPrint)
				print(customer.getCart())
				cprint("Invalid order id. Please try again.", 'red')
				continue
		elif order.lower().startswith("checkout"):
			checkoutStatus = customer.checkout()
			if checkoutStatus:
				print(customer.getReciept())
				sys.exit(0)
			else:
				util.clearLines(customer.cart, customer.itemToPrint)
				print(customer.getCart())
				cprint("You don't have enough money! Try removing a few items.", 'red', attrs=['bold'])
				continue
		else:
			try:
				order = int(order)
				orderStatus = customer.order(order)
				if orderStatus == -1:
					util.clearLines(customer.cart, customer.itemToPrint)
					print(customer.getCart())
					cprint("Invalid order id! Please try again!", 'red')
					continue
				util.clearLines(customer.cart, customer.itemToPrint)
				print(customer.getCart())
				cprint(util.getExcellentChoiceMsg(), 'green', attrs=['bold'])
				continue
			except ValueError:
				util.clearLines(customer.cart, customer.itemToPrint)
				print(customer.getCart())
				cprint("Invalid order id! Please try again!", 'red')
				continue


if __name__ == "__main__":
	main()