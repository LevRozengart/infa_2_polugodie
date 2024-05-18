class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def up_quantity(self, amount):
        self.quantity += amount

    def down_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Ошибка: Недостаточное количество товара.")

    def calculate_total_price(self):
        print(self.price * self.quantity)
        return self.price * self.quantity


product1 = Product("penis", 15, 2)
product1.up_quantity(30)
product1.calculate_total_price()