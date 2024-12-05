import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ch02.ArrayQueue import ArrayQueue


class BTNode:
    def __init__(self, elem, left=None, right=None):
        """ 이진 트리를 위한 노드의 생성자 """
        self.data = elem
        self.left = left    # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크


def preorder(n): # 이진트리의 전위순회 함수
    if n is not None:
        print(n.data, end=' ')  # <- 노드를 방문해 처리할 연산들이 이 자리에 위치. 이 예시에서는 단순 출력만 하는 걸로 설정.
        preorder(n.left)        # 왼쪽 서브 트리 처리
        preorder(n.right)       # 오른쪽 서브 트리 처리

def inorder(n): # 이진트리의 중위순회
    if n is not None:
        inorder(n.left)         # 왼쪽 서브 트리 처리
        print(n.data, end=' ')  # <- 노드에서 처리할 연산들의 위치
        inorder(n.right)        # 오른쪽 서브 트리 처리

def postorder(n): # 이진트리의 후위순회
    if n is not None:
        postorder(n.left)       # 왼쪽 서브 트리 처리
        postorder(n.right)      # 오른쪽 서브 트리 처리
        print(n.data, end=' ')  # <- 노드에서 처리할 연산들의 위치

def levelorder(root):
    queue = ArrayQueue()        # 큐 객체 초기화
    queue.enqueue(root)         # 최초에 루트 노드만 큐에 들어있음.
    while not queue.isEmpty():   # 큐가 공백 상태가 아닌 동안,
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ') # <- 큐에서 하나의 노드를 꺼내고, 이 노드가 None 이 아니면 처리.
            # 이 예시에서는 화면 출력만 함.
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            # 마지막으로 이 노드의 왼쪽과 오른쪽 자식을 큐에 삽입.

def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left) # L 의 높이
    hRight = calc_height(n.right) # R 의 높이
    if (hLeft > hRight):    # 더 큰 값에 + 1(루트노드) 후 반환
        return hLeft + 1
    else: return hRight + 1



# test program

d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n In-Order: ', end=''); inorder(root)
print('\n Pre-Order: ', end=''); preorder(root)
print('\n Post-Order: ', end=''); postorder(root)
print('\n Level-Order: ', end=''); levelorder(root)
print()

print("Node Count = %d개" % count_node(root))
print("Tree Height = %d" % calc_height(root))