"""03-6 이중 연결 구조로 리스트 구현하기"""
class DNode:
    """1) 이중 연결 구조를 위한 노드 클래스"""
    def __init__(self, elem, prev=None, next=None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음 노드를 위한 링크
        self.prev = prev # 이전 노드를 위한 링크 (Linked List와 차이점)

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next= node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node


class DblLinkedList:
    """2) 이중 연결 리스트 클래스"""
    def __init__(self):   # 생성자
        self.head = None  # head 선언 및 None 으로 초기화

    def isEmpty(self): # 공백 상태 검사
        return self.head == None # head 가 None 이면 공백

    def isFull(self): # 포화 상태 검사
        return False # 연결 구조에서는 포화 상태 없음!

    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr

    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None : return None
        else : return node.data

    def display(self, msg='DblLinkedList:'):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>') # 이중연결은 '<=>'로 표시
            ptr = ptr.next
        print('None')

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos-1)
        if before == None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else : before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next # 머리 노드를 삭제하면 "head"가 다음 노드로 변경됨.
            if self.head is not None:
                self.head.prev - None
            return before
        else: before.popNext()