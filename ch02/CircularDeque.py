from ArrayQueue import ArrayQueue

class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10): #생성자는 상속되지 않으므로 다시 구현해야 함.
        super().__init__(capacity) #덱에서 추가되는 데이터는 X, 부모 클래스의 데이터만 초기화.
        # super(): 자식 클래스의 메서드에서 부모를 부르는 함수.

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()
    #deleteFront & getFront 는 전단 요소를 반환해야 하므로 원형 큐의 해당 연산의 결과를 "return" 해야함!

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front-1 + self.capacity) % self.capacity
        # 포화 상태가 아니라면 front에 요소를 삽입
        # & front 를 반시계 방향으로 회전
        else: pass

    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear-1 + self.capacity) % self.capacity
            return item
        # 공백 상태가 아니면 rear 요소를 복사해 두고, rear를 반시계 방향으로 회전.
        # 마지막으로 복사해 둔 요소를 반환.
        else: pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        # 공백이 아니라면 rear 요소를 반환
        else: pass


#2.5 원형 덱의 테스트 프로그램

dq = CircularDeque()

for i in range(9):
    if i%2==0 : dq.addRear(i)
    else : dq.addFront(i)
dq.display("홀수는 전단, 짝수는 후단 삽입")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 2회 삭제, 후단 3회 삭제")

for i in range(9, 14): dq.addFront(i) # 9 ~ 13을 전단으로 삽입
dq.display("전단에 9~ 13 삽입")