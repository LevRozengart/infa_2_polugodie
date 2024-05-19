import pandas as pd
def get_min_value_from_csv(filename: str, column_name: str):
    data = pd.read_csv(filename)
    if column_name in data.columns:
        return data[column_name].min()
    else:
        print(f"Колонка '{column_name}' в файле '{filename}' не найдена")
filename = 'https://gist.githubusercontent.com/sathwika456/485dbd3fa8a1abc348694ae692695fdb/raw/f5202f67da57b3e3875e04682db73e15ac1992ad/weather.csv'
column_name = 'Temperature'
print(get_min_value_from_csv(filename, column_name))
