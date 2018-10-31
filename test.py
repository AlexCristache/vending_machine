import pytest

from vending_machine import VendingMachine
from product import Product

class Test:

    # def __init__(self):
        # self.vending_machine = VendingMachine({'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}, 'products.csv')

    def test_get_total_change(self):
        vending_machine = VendingMachine({'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}, 'products.csv')
        assert vending_machine.get_total_change() == 0

    def test_get_product_by_name(self):
        vending_machine = VendingMachine({'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}, 'products.csv')

        assert isinstance(vending_machine.get_product_by_name('twix'), Product) == True
        assert isinstance(vending_machine.get_product_by_name('MARS'), Product) == True
        assert isinstance(vending_machine.get_product_by_name('kinder'), Product) == False

    def test_dispense_product(self):
        vending_machine = VendingMachine({'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}, 'products.csv')
        products = vending_machine.products_stock.keys()
        product = list(products)[1]
        quantity = vending_machine.products_stock[product]
        vending_machine.dispense_product(product)

        assert vending_machine.products_stock[product] == quantity - 1

    def test_process_change(self):
        vending_machine = VendingMachine({'10': 0, '20': 0, '50': 0, '100': 0, '200': 0}, 'products.csv')
