import util
import Customer
import os
import sys

def main():
    customer = Customer.Customer(
        input("What is your name?\n").lower()
    )

    if customer.isNew:
        return newCustomer(customer)
    else:
        return returningCustomer(customer)

def returningCustomer(customer: Customer.Customer) -> int:
    print(f"Welcome back, \033[32n{customer.name}!\033[0m")
    orderChoice = util.getInt("To make a new order, type in 1. To order previous order, type in 2.")

def newCustomer(customer: Customer.Customer) -> int:
    pass

def orderLoop(customer: Customer.Customer) -> int:
    pass