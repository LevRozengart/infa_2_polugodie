class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            fee = amount * 0.01
            self.balance += (amount - fee)
            print(f"Закинуто: {amount}, Комиссия: {fee}, Баланс: {self.balance:.2f}")
        else:
            print("Нет денег на счету")

    def withdraw(self, amount):
        if amount > 0 and (amount + amount * 0.01) <= self.balance:
            fee = amount * 0.01
            self.balance -= (amount + fee)
            print(f"Снято: {amount}, Комиссия: {fee}, Баланс: {self.balance:.2f}")
        else:
            print("Недостаточно средств")

    def check_balance(self):
        print(f"Текущий баланс: {self.balance}")
        return self.balance

account1 = BankAccount("1251253342", "Lev", 4125)
account1.deposit(2134)
account1.withdraw(5216)
account1.check_balance()