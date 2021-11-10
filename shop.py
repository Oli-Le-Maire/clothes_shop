import psycopg2
from stock import Stock
from config import config

class Interface():

    def greeting(self):
        welcome = input(F"""\n{self.asterix()}\n
        Welcome to Oli's Clothes Shop!!!
        We've only just started up so our website is very
        much still in development, so please bare with us.
        Please type what you would like to do:
        Browse   or    View Basket : \n""")
        welcome = welcome.lower()
        self.options(welcome)

    def asterix(self):
        asterix_string = ""
        for num in range(1, 75):
            asterix_string += "*"
        return (asterix_string)

    def options(self, chosen_option):
        chosen_option = chosen_option
        if chosen_option == "browse":
            self.browse()
        elif chosen_option == "view basket":
            Basket(None).show_basket()
        else:
            print("Oops, you must have made a typo. Let's try again :-)")
            self.greeting()

    def browse(self):
        print(F"""\n {self.asterix()}\n
        Please type in what item you
        would like to buy? For example,
        shirts, trousers, hats...\n""")
        self.choose_item()

    def choose_item(self):
        chosen_item = input(F"""{Interface().asterix()}\n
        Please type which item you would like to view...\n""")
        chosen_item = chosen_item.lower()
        Check_Stock().check_the_item(chosen_item)

    def crossroads_menu(self, buy_option=False):
        if buy_option == False:
            crossroads_question = input(F"""
            {self.asterix()}\n
            What would you like to do?

            HOME | SEARCH AGAIN | VIEW BASKET:

            ENTER YOUR REQUEST HERE: \n
            {self.asterix()}\n
            """)
        else:
            crossroads_question = input(F"""
            {self.asterix()}\n
            What would you like to do?

            HOME | ADD TO BASKET | SEARCH AGAIN | VIEW BASKET:

            ENTER YOUR REQUEST HERE: \n
            {self.asterix()}\n
            """)
        crossroads_answer = crossroads_question.lower()
        self.crossroads_answer_direction(crossroads_answer, buy_option)

    def crossroads_answer_direction(self, crossroads_answer, buy_option):
        print(buy_option)
        if buy_option == True and crossroads_answer == "add to basket":
            print(F"""{Interface().asterix()}

            We should buy...

            but first we have reached an impass.

            NEXT PROGRAMMING STEP: Take shirt away from database and add it to basket AND...

            Separate the classes into individual files

            {Interface().asterix()}

            """)
        elif crossroads_answer == "home":
            Interface().greeting()
        elif crossroads_answer == "search again":
            Interface().choose_item()
        elif crossroads_answer == "view basket":
            Basket(None).show_basket()
        else:
            print("Oops, you have made a typo. Let's try that again...")
            Interface().crossroads_menu()

class Basket():

    def __init__(self, items):
        self.items = items

    def show_basket(self):
        basket = [self.items]
        if basket == [None]:
            print(F"""{Interface().asterix()}\n
            Your basket is currently empty""")
            Interface().greeting()
        else:
            print(basket)


class Check_Stock():

    def check_the_item(self, chosen_item):
        is_item_in_stock = Stock().check_current_stock(chosen_item)
        print(is_item_in_stock)
        if is_item_in_stock[1] == False:
            print(F"\nWe do not have any {chosen_item} in stock\n")
            Interface().crossroads_menu()
        elif is_item_in_stock[1] == True:
            print(F"""\nWe have {is_item_in_stock[0][1]} in stock...\n
            {is_item_in_stock[0][1]}: £{is_item_in_stock[0][2]}\n""")
            Interface().crossroads_menu(True)
        else:
            print("Error")





Stock().create_table()
Interface().greeting()
# Stock().row_to_add_in_stock("shirts", 22.99)
# Stock().remove_chosen_item_from_stock("shirts")
