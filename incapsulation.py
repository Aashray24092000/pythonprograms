class bank_acc():
    def __init__(self,balance):
        self.__balance=balance
        
    def deposite(self,amount):
        self.__balance=self.__balance + amount
        
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance=self.__balance-amount
            return True
        else:
            False
            
    def get_balance(self):
        return self.__balance
