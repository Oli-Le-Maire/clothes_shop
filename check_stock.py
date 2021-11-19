from stock import Stock

class Check_Stock():

    def check_the_item(self, chosen_item):
        is_item_in_stock = Stock().check_current_stock(chosen_item)
        if is_item_in_stock[1] == False:
            return (is_item_in_stock)
        elif is_item_in_stock[1] == True:
            return (is_item_in_stock)
