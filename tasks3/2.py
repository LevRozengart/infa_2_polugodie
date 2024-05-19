import csv
with open('../data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Фамилия", "Возраст"])
    writer.writerow(['Журавский', "Георгий", 27])
def print_file(filename: str):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
print_file('../data.csv')
