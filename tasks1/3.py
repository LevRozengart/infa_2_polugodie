
dop_array = [char for char in input() if char.isalnum()]
if dop_array == dop_array[::-1]:
    print(True)
else:
    print(False)