def evaluate(node):
    """ 수식 트리 계산함수 """
    if node is None:        # 공백 트리이면 -> 0 반환
        return 0
    elif node.isLeaf():     # 단말노드이면 -> 피연산자
        return node.data
    else:                   # 루트나 가지노드라면 -> 연산자
        op1 = evaluate(node.left)   # 왼쪽 & 오른쪽 서브트리를 먼저 계산해야 루트를 계산 가능.
        op2 = evaluate(node.right)

        # 현재노드를 처리. 후위순회
        if node.data == '+':
            return op1 + op2
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2

from BinaryTree import *
def buildETree(expr):
    """ 후위표기 식으로 수식트리 만들기"""
    if len(expr) == 0:
        return None

    token = expr.pop()  # 후위순회는 수식을 뒤에서 앞으로 처리. pop() -> 맨 뒤의 요소를 꺼냄
    if token in "+-*/":
        # 연산자이면 노드를 만들고, 오른쪽 -> 왼쪽 순으로 서브트리를 순환 호출을 이용해 만듦.
        # 마지막으로 노드 반환.
        node = BTNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else:
        # 피연산자이면 단말노드이므로 노드를 만들어 바로 반환.
        return BTNode(float(token))

##############################
# 테스트 프로그램
str = input("입력(후위표기): ")     # 후위표기식 입력
expr = str.split()               # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)

root = buildETree(expr)          # 후위표기식을 수식 트리로 제작 & 루트를 반환
print('\n 전위순회: ', end=''); preorder(root)
print('\n 중위순회: ', end=''); inorder(root)
print('\n 후위순회: ', end=''); postorder(root)
print('\n 계산결과: ', evaluate(root))      # 수식 트리 계산
