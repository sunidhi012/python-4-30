from BankClass import Bank
from storage import all_accounts
from Functions import findAccountByNumber
from ExceptionHandling import DepositError, WithdrawError

def main_runnable_code():
    while True:
        print('Welcome to Bank Application')
        print('1. Create Account')
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. Show Details')
        print('5. Exit')

        try:
            choice = int(input('Enter your choice (1 - 5):'))
            
            if choice == 1:
                yn = input('Do you really want to create account? (y/n):')
                if yn == 'y':
                    name = input('Enter customers full name.')
                    init_balance = int(input('Enter initial balance:'))
                    
                    if init_balance > 100:
                        b = Bank(name, init_balance)
                        all_accounts.append(b)
                        print(f'Account created with name {name} and account number {b.account_number}.')
                        print(f'Rs. {init_balance} deposited to A/C no. {b.account_number}')
                    else:
                        print(f'Initial deposit balance must be more than Rs.100.')
                elif yn == 'n':
                    print('Continue with your transaction.')
                else:
                    print('Only enter y/n.')
                    
            # Deposit Amount Section   
            elif choice == 2:
                yn = input('Do you really want to deposit amount? (y/n):')
                if yn == 'y':
                    acc_number = input('Enter your account number:')
                    find_acc = findAccountByNumber(acc_number)

                    if find_acc: # if find_acc has any value....
                        amount = int(input('Enter deposit amount: '))
                        try:
                            find_acc.deposit(amount)
                        except DepositError as e:
                            print(e)
                    else:
                        print('No account found with provided account number.')
                elif yn == 'n':
                        print('Continue with your transaction.')
                else:
                    print('Only enter y/n.')

            # Withdraw Amount Section   
            elif choice == 3:
                yn = input('Do you really want to withdraw amount? (y/n):')
                if yn == 'y':
                    acc_number = input('Enter your account number:')
                    find_acc = findAccountByNumber(acc_number)

                    if find_acc:
                        amount = int(input('Enter withdraw amount: '))
                        try:
                            find_acc.withdraw(amount)
                        except WithdrawError as e:
                            print(e)
                    else:
                        print('No account found with provided account number.')
                elif yn == 'n':
                    print('Continue with your transaction.')
                else:
                    print('Only enter y/n.')
            
            # Show Detail Section
            elif choice == 4:
                yn = input('Do you really want to see account details? (y/n):')
                if yn == 'y':
                    acc_number = input('Enter your account number:')
                    find_acc = findAccountByNumber(acc_number)

                    if find_acc:
                        find_acc.show_details()
                    else:
                        print('No account found with provided account number.')
                elif yn == 'n':
                    print('Continue with your transaction.')
                else:
                    print('Only enter y/n.')
                        
            # Program Exit Section   
            elif choice == 5:
                print('Thank you for choosing us.')
                break
            else:
                print('Invalid Input.')
        except ValueError:
            print('Error: Please enter only value from 1 to 5.\n')