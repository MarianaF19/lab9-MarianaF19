# person.py

class Person:
    def _init_(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def _str_(self):
        return f"Name = {self.name}, Number of accounts = {len(self.accounts)}"