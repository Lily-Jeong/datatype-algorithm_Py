""" 03-5 단순 연결 구조로 리스트 구현하기 """

class Node:
    def __init__(self, elem, link=None): # default 값 : None
        """1. 단순 연결 노드의 생성자"""
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링크 생성 및 초기화

    def append(self, node): #self 다음에 node를 넣는 연산
        """2. 새로운 노드를 현재 노드인 self 뒤에 추가하는 append()연산 구현"""
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        """3. self 다음 노드를 삭제하는 연산"""
        next = self.link
        if next is not None:
            self.link = next.link
        return next


class LinkedList:
    def __init__(self):
        """4. head 선언 및 None으로 초기화"""
        self.head = None

    """5. 공백 상태와 포화 상태 검사하는 연산 구현"""
    def isEmpty(self): # 공백 상태 검사
        return self.head == None # head 가 None 이면 공백

    def isFull(self): # 포화 상태 검사
        return False # 연결 구조에서는 포화 상태 없음!

    def getNode(self, pos):
        """6. pos 번째 노드를 반환하는 getNod(pos) 연산"""
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr

    def getEntry(self, pos):
        """7.pos 번째 노드의 요소를 반환하는 연산"""
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None : return None
        else : return node.data

    def insert(self, pos, e):
        """8. pos 위치에 새로운 요소를 삽입하는 insert(pos, e) 연산"""
        node = Node(e, None)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head
            self.head = node
        else : before.append(node)

    def delete(self, pos):
        """9. pos 위치의 요소를 삭제하는 delete(pos) 연산"""
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else: return before.popNext()

    def size(self):
        """10. 전체 요소의 수를 구하는 size() 연산"""
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

    def display(self, msg='LinkedList:'):
        """11. 리스트를 화면에 출력하는 display()연산"""
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            prt = ptr.link
        print('None')
