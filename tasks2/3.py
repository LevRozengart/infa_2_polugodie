class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        a = self.a
        b = self.b
        c = self.c
        try:
            if a > 0 and b > 0 and c > 0:
                if a + b > c and a + c > b and b + c > a:
                    print('Ура, можно постороить треугольник')
                else:
                    print('Жаль, но из этого треугольника сделать')
            else:
                return print('С отрицательными числами ничего не выйдет')
        except TypeError:
            print('Нужно вводить только числа!')
a = TriangleChecker(3, 4, 5).is_triangle()
