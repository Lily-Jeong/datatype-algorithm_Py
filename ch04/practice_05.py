# 중위표기 수식 => 후위표기 수식 변환 방법
# 스택 사용

# 연산자의 우선순위 계산 함수
def precedence(op):
    if (op == '(' or op == ')') : return 0
    elif (op == '+' or op == '-') : return 1
    elif (op == '*' or op == '/') : return 2
    else: return -1

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch01.StackClass import ArrayStack


# 중위 표기 수식의 후위식 변환
def in_fix_to_post_fix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else: # 피연산자
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())

    return output
