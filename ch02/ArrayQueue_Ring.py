from ArrayQueue import ArrayQueue


#2.3b 링 버퍼의 테스트 프로그램
q = ArrayQueue(8) # 큐 객체 생성 (capacity=8)

q.display("초기 상태")
for i in range(6):
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6); q.enqueue2(7)
q.display("삽입 6,7")

q.enqueue2(8); q.enqueue2(9)
q.display("삽입 8,9")


q.dequeue(); q.dequeue()
q.display("삭제  x2")