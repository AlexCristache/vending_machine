# vending_machine
This project aims to simulate a vending machine. It comprises a Product class
and a VendingMachine class with the latter doing most of the work. The initial
state of the vending machine consists of the amount of change available at the
start(which is passed as a parameter to be tweaked by the user) and a list of
products which is read from a CSV file. The structure of the file is made up from
three columns(name, price(in pennies) and available quantity).

The machine runs forever and on each cycle it displays a list of the products with
their respective names, prices(in GBP this time for readability) and the available
quantity at that point in time. It supports multiple item selection as well.
After a user has made a selection, it asks if there will be another purchase or not.
Afterwards the machine prompts the user to insert coins in order to make the payment.
As the coins are inserted into the machine, the 'credit' is updated and at the end
the machine provides the right amount of change if it has sufficient funds.

# This project was developed using python 3.7.0

# In order to run the project, simply run python vending_machine.py
