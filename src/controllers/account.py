from models.account import Account
from models.transaction import Transaction


class AccountController():
    def __init__(a : Account):
        self.acccount = a
    
    def add_transaction(
        transaction_id: str,
        account_transaction_id: str,
        value: float,
        category: str,
        description: str,
        transaction_date: str,
    ):
        t = Transaction(
            name=name, 
            value=value, 
            category=category, 
            description=description,
            account=self.account,
        )
        t.save()

    def get_transactions():
        return self.account.transactions

    def get_transactions_since():
        pass

    def delete_transaction(id):
        pass
