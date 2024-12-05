# 왼쪽 자식 - 오른쪽 형제 표현을 위한 노드 클래스 정의

class CS_Node:
    def __init__(self, elem, child=None, sibling=None):
        self.data = elem
        self.child = child
        self.sibling = sibling
