a, b = int(input()), int(input())
dop_array = list()
for i in range(a, b+1):
    if i > 1:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            dop_array.append(i)
    else:
        continue
print(sum(dop_array))