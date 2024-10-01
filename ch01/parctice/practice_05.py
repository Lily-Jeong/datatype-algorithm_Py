values = list()

for i in range(20):
    if i % 3 == 0:
        values.append(i)
        print(values)
    elif i % 4 == 0:
        values.pop()
        print(values)