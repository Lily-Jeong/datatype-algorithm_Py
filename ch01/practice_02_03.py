class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        # self.top = -1
        # Q: 스택을 공백 상태로 초기화하는 clear() 연산을 추가해보세요.
        def clear(self):
            self.top = -1

        def display(self):
            for i in range(0, self.top+1):
                print(self.array[i], end='')
            print()