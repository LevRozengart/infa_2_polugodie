import csv
for_sr = 0
with open('C:/Users/levko/PycharmProjects/1/example_1kb.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for col in row:
            data = col.split(',')
            for char in data:
                for_sr += int(char)
            print(for_sr / len(data))
