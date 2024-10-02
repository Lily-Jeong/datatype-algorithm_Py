import queue
import random

q = queue.Queue(8)

print("삽입 순서: ", end=' ')
while not q.full() :
    v = random.randint(0, 100)
    q.put(v)
    print(v, end=' ')
    # 큐가 포화 상태가 될 때까지 0에서 99 사니의 정수를 무작위로 발생하여 큐에 삽입.
print()

print("삭제 순서: ", end=' ')
while not q.empty() :
    print(q.get(), end=' ')
    #큐가 공백 상태가 될 때까지 요소를 꺼내서 화면에 출력
print()

#########

import collections
dq = collections.deque() # 덱 객체 생성

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")
for i in range(9):
    if i%2==0 : dq.append(i)
    else: dq.appendleft(i)
    # i는 0부터 8까지 순서대로 대입됨. i가 짝수면 후단, 홀수면 전단으로 삽입.
print("홀수는 전단, 짝수는 후단 삽입", dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 2회 삭제, 후단 3회 삭제", dq)

for i in range(9, 14): dq.appendleft(i) # 9~13을 전단으로 삽입
print("전단에 9 ~ 13 삽입     ", dq)

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")