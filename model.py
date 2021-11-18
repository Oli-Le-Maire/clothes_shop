import psycopg2
from stock import Stock
from basket import Basket
from check_stock import Check_Stock
from config import config

class Model():

    def check_the_stock(self, chosen_item):
        stock_info = Check_Stock().check_the_item(chosen_item.lower())
        if stock_info[1] == False:
            print(F"\nWe do not have any {chosen_item} in stock\n")
            return chosen_item
        elif stock_info[1] == True:
            formatted_item_check = []
            formatted_item_check += stock_info[0]
            return formatted_item_check
        else:
            print("Error")

    def show_basket_text(self):
        if Basket(None).show_basket()[1] == False:
            print(F"""
            Your basket is currently empty""")
            Model().greeting()
        elif Basket(None).show_basket()[1] == True:
            print(basket)
        else:
            print("Error")
