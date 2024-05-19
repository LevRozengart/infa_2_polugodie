class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        if subject in self.subjects:
            del self.subjects[subject]
        else:
            print(f'Предмет {subject} отсутствует в списке предметов студента {self.name}.')

    def calc_average(self):
        sum_grades = sum(self.subjects.values())
        if len(self.subjects) == 0:
            return 0
        else:
            return sum_grades / len(self.subjects)

# Создаем объекты класса Student
student1 = Student("Иванов", 15)
student1.add_subject("Математика", 5)

# Проверяем функциональность класса
print(f"Средний балл студента {student1.name}: {student1.calc_average()}")

student1.remove_subject("Математика")
