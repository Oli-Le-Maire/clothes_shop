class Basket():

    def __init__(self, items):
        self.items = items

    def show_basket(self):
        basket = [self.items]
        if basket == [None]:
            return (basket, False)
        else:
            return (basket, True)
