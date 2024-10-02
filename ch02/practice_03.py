from ArrayQueue import ArrayQueue

values = ArrayQueue()

for i in range(20):
    if i % 3 == 0:
        values.enqueue(i)
    elif i % 4 ==0:
        values.dequeue()

print(values)


# 9 12 15 18