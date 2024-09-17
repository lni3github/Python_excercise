from random import randint
class Account():
    #database
    #{account_number: "0001", name: "Jeff Doram" ,balance: 9000}
    account = {}

    #เปิดบัญชี
    def __init__(self, name:str, deposit:int):
        self.__account_number = randint(1, 99999)
        self.name = name
        self.__balance = deposit

    def deposit(self, deposit_amount:int):
        self.__balance = self.__balance + deposit_amount
        print(f"deposit: {deposit_amount}")
        self.balance()

    def withdraw(self, withdraw_amount:int):
        if self.__balance >= withdraw_amount:
            self.__balance = self.__balance - withdraw_amount
            print(f"withdraw: {withdraw_amount}")
            self.balance()
        else:
            print("not enough funds!")
        
    def balance(self):
        print(f"your current account balance: {self.__balance}")

    def information(self):
        print(f"Account No.: {self.__account_number}, Name: {self.name}, Current balance: {self.__balance}")

#regis account
account1 = Account("Boss Navamin", 5000)

account1.information()