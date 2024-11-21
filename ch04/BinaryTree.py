class BTNode:
    def __init__(self, elem, left=None, right= None):
        """ 이진 트리를 위한 노드의 생성자 """
        self.data = elem
        self.left = left    # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크