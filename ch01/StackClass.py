class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity            # 스택 용량
        self.array = [None]*self.capacity   # 요소 배열
        self.top = -1                       # 상단의 인덱스
    # 1.2b: 스택 클래스의 연산
    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity-1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else: pass                          # overflow 예외는 처리하지 않았음

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass                          # underflow 예외는 처리하지 않았음

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass                          # underflow 예외는 처리하지 않았음

    def size() : return top+1

s = ArrayStack(100)

msg = input("문자열 입력: ")
for c in msg:
    s.push(c)

print("문자열 출력: ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()