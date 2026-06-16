import random 
from datetime import datetime
from ExceptionHandling import DepositError, WithdrawError

class Bank:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
        self.account_number = "".join(str(random.randint(0,9)) for i in range(16))
        self.created_at = datetime.now()

    #Deposit Function
    def deposit(self, amount):
        if amount > 100:
            self.balance += amount
            print(f'Rs. {amount} deposited to A/C n0. {self.account_number}.')
        else:
            raise DepositError ('Deposit amount must be more than 100.')

    #Withdraw Function
    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balane:
                self.balance -= amount
                print(f'Rs. {amount} withdrawn from A/C no. {self.account_number}.')
            else:
                raise WithdrawError('Withdraw amount must be lower than balance amount.')
        else:
            print('Withdrawn amount must be higher than 0.')
            
    def show_details(self):  
        print('Account Details')
        print('-'*35)
        print(f'Account Name: {self.account_name}')
        print(f'Account Balance: Rs.{self.balance}')
        print(f'Account Number: {self.account_number}')
        print(f'Account Created At: {self.created_at}')