# class Check_Stock():
#
#     def __init__(self):
#         self.stock_dict = {
#             "T-shirts": [1],
#             "Trousers": [2],
#             "Skirts": [0],
#             "Hats": [4]
#   }
#
#     def format_current_stock(self):
#         current_stock = ""
#         for key, value in self.stock_dict.items():
#             if value != 0:
#                 current_stock += (key + "\n")
#             else:
#                 current_stock += (key + " (Out of stock)\n")
#         return current_stock
#
#     def show_item_stock(self, chosen_item):
#         counter = 0
#         for keys, values in self.stock_dict.items():
#             values.append(keys.lower())
#         for clothes, clothes_value in self.stock_dict.items():
#             if clothes_value[1] == chosen_item:
#                 print(F"""{Interface().asterix()}\n
#                 We have {self.stock_dict[clothes][0]} {chosen_item}""")
#                 counter += 1
#                 Interface().greeting()
#         if counter == 0:
#             print(F"""\n{Interface().asterix()}
#                 \nYour search, '{chosen_item}', did not match any of our stock,
#                 please check your request and
#                 try again...\n""")
#             Interface().choose_item()
