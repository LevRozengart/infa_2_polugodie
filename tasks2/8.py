import math
class Tochka:
    def __init__(self, x, y):
        self.array = list()
        self.array.append([x, y])

    def add_t(self, x, y):
        self.array.append([x, y])
        return self.array

    def rasstoyanie(self):
        print(((abs(self.array[1][0] - self.array[0][0]) ** 2 + abs(self.array[1][1] - self.array[0][1]) ** 2) ** 0,5))
        return ((abs(self.array[1][0] - self.array[0][0]) ** 2 + abs(self.array[1][1] - self.array[0][1]) ** 2) ** 0,5)

    def peremesti(self, x_s, y_s):
        self.array[0][0] += x_s
        self.array[0][1] += y_s
        return self.array

    def check_os(self):
        if self.array[0][0] == 0 or self.array[0][1] == 0:
            print('Принадлежит')
            return True
        else:
            print('Не принадлежит')
            return False

t = Tochka(1, 2)
t.add_t(3, 4)
t.rasstoyanie()