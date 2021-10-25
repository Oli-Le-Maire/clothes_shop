class Interface():

    def greeting(self):
        welcome = input(F"""\n{self.asterix()}\n
        Welcome to Oli's Clothes Shop!!!
        We've only just started up so our website is very much still in development, so please bare with us.
        Please type what you would like to do:     Browse   or    View Basket : \n""")
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
            print("Error")

    def browse(self):
        print(F"""\n {self.asterix()}\n
            We have the following to choose from?""")
        print(F"{Stock().format_current_stock()}")
        self.choose_item()

    def choose_item(self):
        chosen_item = input(F"""{Interface().asterix()}\n\nPlease type which item you would like to view...\n""")
        chosen_item = chosen_item.lower()
        Stock().show_item_stock(chosen_item)


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


class Stock():

    def __init__(self):
        self.stock_dict = {
            "T-shirts": [1],
            "Trousers": [2],
            "Skirts": [0],
            "Hats": [4]
  }

    def format_current_stock(self):
        current_stock = ""
        for key, value in self.stock_dict.items():
            if value != 0:
                current_stock += (key + "\n")
            else:
                current_stock += (key + " (Out of stock)\n")
        return current_stock

    def show_item_stock(self, chosen_item):
        counter = 0
        for keys, values in self.stock_dict.items():
            values.append(keys.lower())
        for clothes, clothes_value in self.stock_dict.items():
            if clothes_value[1] == chosen_item:
                print(F"""{Interface().asterix()}\n
                We have {self.stock_dict[clothes][0]} {chosen_item}""")
                counter += 1
                Interface().greeting()
        if counter == 0:
            print(F"""\n{Interface().asterix()}\nYour search, '{chosen_item}', did not match any of our stock, please check your request and try again...\n""")
            Interface().choose_item()


class DatabaseTest():

    def connect_to_database():
        conn = psycopg2.connect(
            host="localhost",
            dbname="stock",
            user="postgres",
            password="password")
#port number defaults to 5432 if not specified in variables above


Interface().greeting()
