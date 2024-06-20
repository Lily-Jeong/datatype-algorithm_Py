# 1.1a: 스택을 위한 데이터
capacity = 10
array = [None]*capacity
top = -1

# 1.1b: 스택의 공백 상태와 포화 상태 검사
def isEmpty():
    if top == -1 : return True
    else : return False

def isFull() : return top == capacity-1

# 1.1c: 스택 삽입 연산
def push(e):
    #global top
    if not isFull():    # 포화 상태가 아닌 경우
        top += 1        # top 증가 (global top 선언 필요)
        array[top] = e  # top 위치에 e 복사
    else:
        print("stack overflow")
        exit()

#1.1d: 스택의 삭제 연산
def pop() :
    # global top
    if not isEmpty():   # 공백 상태가 아닌 경우
        top -= 1        # top 감소 (global top 선언 필요)
        return array[top+1] # 이전(top+1) 위치의 요소 반환
    else:
        print("stack underflow")
        exit()

#1.1e: 스택의 peek() 연산
def peek():
    if not isEmpty():       # 공백 상태가 아닌 경우
        return array[top]
    else: pass              # underflow 예외는 처리하지 않았음

#1.1f: 스택의 size() 연산
def size() : return top+1   # 현재 요소의 수는 top+1
