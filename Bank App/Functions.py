from storage import all_accounts

def findAccountByNumber(acc_number):
    for account in all_accounts:
        if acc_number == account.account_number:
            return account
        return None