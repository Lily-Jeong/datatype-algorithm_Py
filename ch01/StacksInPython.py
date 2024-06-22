""" s = list()

msg = input("Type in string: ")
for c in msg:
    s.append(c)

print("Type in string: ", end='')
while len(s) > 0:
    print(s.pop(), end='')

print() """

import queue

s = queue.LifoQueue(maxsize=100)

msg = input("Type in string: ")
for c in msg:
    s.put(c)

print("Type in string: ", end='')
while not s.empty():
    print(s.get(), end='')
print()