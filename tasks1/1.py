array = input().split()
mn = set(array)
dop_array = [char for char in mn if char.isalpha()]
print(*sorted(dop_array))
