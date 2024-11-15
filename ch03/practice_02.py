# My answer
from LinkedList import LinkedList, Node

def find(obj, list):
    a = 0
    for i in range(0, len(list)):
        if obj == list[i]:
            a = i
        else:
            a = -1
    return a

#test 1
li_1 = ['a','b','c','d','e']
find('e', li_1) # => answer: 4

li_2 = [1,2,3,4,5]
find('e', li_2) # => answer: -1


# Answer sheet
"""
def find(self, e):
    node = self.head
    pos = 0 # head 의 인덱스를 0이라 가정
    while node is not None:
        if node.data == e:
            return pos
        node = node.link
    return -1

"""