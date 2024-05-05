class Soda:
    def __init__(self, dobavka=1):
        self.dobavka = dobavka
    def show_my_drink(self):
        if self.dobavka != 1:
            return f'Газировка и {self.dobavka}'
        else:
            return 'Обычная газировка'

cola = Soda('краситель')
print(cola.show_my_drink())
