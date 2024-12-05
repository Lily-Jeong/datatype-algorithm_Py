
table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
    ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
    ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..'),
]

class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right


def encode(ch):
    """ 모스 코드 인코딩 함수"""
    idx = ord(ch.upper())-ord('A') # 리스트에서 해당 문자의 인덱스
    return table[idx][1]   # 해당 문자의 모스 부호 반환

def decode_simple(morse):
    """ 단순한 방법의 모스 코드 디코딩 함수"""
    for tp in table:        # 모스 코드 표의 모든 문자에 대해
        if morse == tp[1]:  # 찾는 코드와 같으면
            return tp[0]    # 그 코드의 문자를 반환
    # => 표 크기(문자 수)가 n개라면 n 번 비교해야 함 -> 매우 비효율적인 방법!

def make_morse_tree():
    """ 모스 코드 디코딩을 위한 결정 트리 만들기 """
    root = TNode( None, None, None )
    for tp in table:        # tp: 모스 코드 표의 각 항목
        code = tp[1]        # tp[1]: 모스 코드
        node = root         # 루트부터 탐색
        for c in code:
            if c == '.':
                # 왼쪽 자식이 비었으면 빈 노드를 추가.
                if node.left == None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                # 왼쪽과 동일한 방법으로 오른쪽도 진행.
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]   # 최종 노드에 문자(tp[0]) 부여
    return root

def decode(root, code):
    """ 결정 트리를 이용한 디코딩"""
    node = root                             # 루트 노드에서 시작
    for c in code:                          # 각 부호에 대해
        if c == '.' :
            node = node.left      # 점(.): 왼쪽으로 이동
        elif c == '-' :
            node = node.right   # 선(-): 오른쪽으로 이동
    return node.data                        # 문자 반환




morseCodeTree = make_morse_tree()   # 모스코드 결정 트리를 만듦. morseCodeTree = root
str = input("입력 문장 : ")
mlist = []
for ch in str:
    # 입력 문자열의 각 문자들을 순서대로 모스코드로 변환하여 리스트에 추가.
    code = encode(ch)
    mlist.append(code)

print("Morse Code: ", mlist)
print("Decoding: ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()
