""" System imports """
import csv
import typing

""" Local imports """
from product import Product

class VendingMachine:

    products_stock = {}

    def __init__(self):
        self.change_amount = {'10p': 100, '20p': 50, '50p': 50, '100p': 25}

    def is_product_in_stock(self, product_name: str):
        if len(self.products_stock) > 0:
            for key in self.products_stock.keys():
                if key.name == product_name:
                    return True
        else:
            return False

    def get_product_by_name(self, product_name: str):
        if len(self.products_stock) > 0:
            for product in self.products_stock.keys():
                if product.name == product_name:
                    return product
            else:
                return "Product does not exist"
        return "No products in stock"

    def add_product_stock(self, product: Product, quantity: int):
        in_stock = self.is_product_in_stock(product.name)
        if in_stock:
            product = self.get_product_by_name(product.name)
            self.products_stock[product] += quantity
        else:
            self.products_stock[product] = quantity


def main():
    vending_machine = VendingMachine()
    with open('products.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            product = Product(row[0], row[1])
            # products[product] = row[2]
            vending_machine.add_product_stock(product, int(row[2]))
    products = vending_machine.products_stock
    for key, value in products.items():
        print(f'name = {key.name} price = {key.price} stock = {value}')



if __name__ == "__main__":
    main()
