# N-링크 표현을 위한 노드 클래스 정의
# 링크의 저장을 위해 연결 리스트를 사용.

class N_Node:
    def __init__(self, elem):
        self.data = elem
        self.link = []

    def addChild(self, node):
        self.link.append(node)