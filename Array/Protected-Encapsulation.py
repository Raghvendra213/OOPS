class Account:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
        print(self.__balance)
a1 = Account(20000)
a1.show_balance()
    