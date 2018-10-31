""" System imports """
import csv
import typing

""" Local imports """
from product import Product

class VendingMachine:

    products_stock = {}

    """
    initialise the vending machine with a change amount and a CSV file from which
    the products are read. The CSV file follows a name, price(in pennies), quantity
    structure
    """
    def __init__(self, change_pool: dict, file_path: str):
        self.change_amount = change_pool
        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                product = Product(row[0], float(row[1]))
                self.add_product_stock(product, int(row[2]))

    def print_change_pool(self):
        for coin, amount in self.change_amount.items():
            print(f'coin = {int(coin)/100}GBP; amount = {amount}')

    """
    Calculates the total amount of change available in the machine
    """
    def get_total_change(self):
        sum = 0
        for key, value in self.change_amount.items():
            if key == '10p':
                sum += 10 * value
            if key == '20p':
                sum += 20 * value
            if key == '50p':
                sum += 50 * value
            if key == '100p':
                sum += 100 * value
        return sum

    def is_product_in_stock(self, product_name: str):
        if len(self.products_stock) > 0:
            for key in self.products_stock.keys():
                if key.name.lower() == product_name.lower():
                    return True
        else:
            return False

    def get_product_by_name(self, product_name: str):
        if len(self.products_stock) > 0:
            for product in self.products_stock.keys():
                if product.name.lower() == product_name.lower():
                    return product
            else:
                return "Product does not exist"
        return "No products in stock"

    """
    adds a product to the vending machine stock and if that product is already
    available on the machine, it just updates the quantity
    """
    def add_product_stock(self, product: Product, quantity: int):
        if quantity < 0:
            print("Quantity can't be a negative number")
            return
        in_stock = self.is_product_in_stock(product.name)
        if in_stock:
            product = self.get_product_by_name(product.name)
            self.products_stock[product] += quantity
        else:
            self.products_stock[product] = quantity

    def make_selection(self, product_name: str):
        return self.get_product_by_name(product_name)


    """
    when a product is dispensed, the stock needs to be updated
    """
    def dispense_product(self, product: Product):
        self.products_stock[product] -= 1


    """
    decide how to issue the change to the user with preference for the higher
    value coins first
    """
    def process_change(self, amount: int):
        change_coins = {'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}
        while amount >= 200 and self.change_amount['200'] > 0:
            amount -= 200
            change_coins['200'] += 1
            self.change_amount['200'] -= 1
        while amount >= 100 and self.change_amount['100'] > 0:
            amount -= 100
            change_coins['100'] += 1
            self.change_amount['100'] -= 1
        while amount >= 50 and self.change_amount['50'] > 0:
            amount -= 50
            change_coins['50'] += 1
            self.change_amount['50'] -= 1
        while amount >= 20 and self.change_amount['20'] > 0:
            amount -= 20
            change_coins['20'] += 1
            self.change_amount['20'] -= 1
        while amount >= 10 and self.change_amount['10'] > 0:
            amount -= 10
            change_coins['10'] += 1
            self.change_amount['10'] -= 1
        if self.get_total_change() < amount:
            print('Insufficient funds to give change. We are terribly sorry :(')
        return change_coins


    """
    capture the user's coin input and update the change amount in the machine
    accordingly
    """
    def insert_coins(self, coins: dict, cash_paid: float):
        for coin, amount in coins.items():
            coins[coin] = int(input(f'How many {int(coin)/100}GBP coins would you like to insert?\n>> '))
            cash_paid += int(coin) * coins[coin]
            self.change_amount[coin] += coins[coin]
            print(f'Current credit = {cash_paid/100}GBP')
        return cash_paid


def main():
    change_pool = {'10': 100, '20': 100, '50': 20, '100': 20, '200': 10}
    vending_machine = VendingMachine(change_pool, 'products.csv')
    total_change = vending_machine.get_total_change()
    products = vending_machine.products_stock
    while True:
        print('Available change pool')
        vending_machine.print_change_pool()
        print('New purchase')
        print('Available products:')
        print('Product | Price | Available quantity')
        print('--------------------------------')
        for key, value in products.items():
            print(f'{key.name} | {key.price/100}GBP | {value}')

        buy = True
        selections = []
        amount_due = 0
        while buy:#let the user make multiple purchases in one go
            selection = vending_machine.make_selection(input('Make selection\nName: '))
            while not isinstance(selection, Product):
                selection = vending_machine.make_selection(input('Invalid selection. Please try again: '))
            else:
                while products[selection] <= 0:
                    selection = vending_machine.make_selection(input('Product is not in stock. Please choose another product: '))
            amount_due += selection.price
            selections.append(selection)
            print('-----------------------')
            print('Current selected products')
            for s in selections:
                print(s.name)
            print(f'Amount due: {amount_due/100}GBP')
            choice = input('Would you like to purchase anything else?(yes/no) ')
            while choice.lower() != 'no' and choice.lower() != 'yes':
                choice = input('Invalid!!! Please choose Yes or No ')
            if choice.lower() == 'no':
                break

        print('Please insert coins(only multiple of 10 allowed):')
        coins = {'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}
        cash_paid = vending_machine.insert_coins(coins, 0)

        while cash_paid < amount_due:
            print(f'Amount left:{(amount_due - cash_paid)/100}GBP')
            cash_paid = vending_machine.insert_coins(coins, cash_paid)
        else:
            print(f'Change due: {(cash_paid - amount_due)/100}GBP')
            change = cash_paid - amount_due
            change_coins = vending_machine.process_change(change)
            for coin, amount in change_coins.items():
                print(f'{amount} x {float(coin)/100}GBP given back')
            for s in selections:
                vending_machine.dispense_product(s)
        print()

if __name__ == "__main__":
    main()
