def find_max( A ):
    n = len(A)  # 입력의 크기
    max = A[0]  # max 초기화 -> 입력받은 리스트의 첫번째 요소를 할당.
    for i in range(n):
        if A[i] > max:
            max = A[i]  # 반복문 내부 -> n 번 반복(가장 많이 처리)
    return max

def find_key(A, key):
    n = len(A)
    for i in range(n):
        if A[i] == key: # 탐색 성공
            return i    # 해당 인덱스 반환
    return -1           # 탐색 실패 --> -1 반환