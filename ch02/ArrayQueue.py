#02-2
    #2.1a 클래스의 선언과 멤버 변수 초기화

class ArrayQueue:
    def __init__(self, capacity = 10): #생성자 정의
        self.capacity = capacity #용량(고정)
        self.array = [None] * capacity #요소들을 저장할 배열
        self.front = 0 #전단 인덱스
        self.rear = 0 #후단 인덱스

    #2.1b 공백 상태와 포화 상태를 검사하는 isEmpty() & isFull()
    def isEmpty(self): # 공백상태
        return self.front == self.rear

    def isFull(self): # 포화상태
        return self.front == (self.rear +1)%self.capacity

    #2.1c 원형 큐: 삽입 연산
    def enqueue(self, item): # 삽입 연산
        if not self.isFull(): # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass
            # 언더플로 예외 처리는 생략 -> 예외 상황에 대한 처리는 응용에 따라 달라질 수 있기 때문.

    #2.1d 원형 큐: 삭제 연산 (맨 앞의 요소 삭제)
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass # overflow 오류 처리 생략

    #2.1e 원형 큐: 상단 들여다보기 연산
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass # underflow 오류 처리 생략

    #2.1f 원형 큐: 전체 요소의 수
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    #2.1g 원형 큐: 전체 요소를 화면으로 출력
    def display(self, msg):
        print(msg, end='= [')
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i%self.capacity], end=' ')
        print("]")

    #2.3a 원형 큐: 링 버퍼를 위한 삽입 연산
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty(): # front == rear
            self.front = (self.front + 1) % self.capacity
            #삽입 후가 공백이면 오류 상태. 이 경우 front를 회전시켜 가장 오래된 요소를 삭제.

    #practice Q2. 원형 큐 클래스에 큐를 공백 상태로 초기화하는 clear() 연산을 추가.
    # def clear(self):
    #     if not self.isEmpty():
    #         self.array = [None]
    #     else: pass
    #해답
    def clear(self):
        self.front = 0
        self.rear = 0

#2.2 원형 큐: 테스트 프로그램
# import random # 난수 발생 목적
# q = ArrayQueue(8)
# q.display("초기 상태")
# while not q.isFull():
#     q.enqueue(random.randint(0,100))
# q.display("포화 상태")

# print("삭제 순서: ", end=' ')
# while not q.isEmpty():
#     print(q.dequeue(), end=' ')
# print()