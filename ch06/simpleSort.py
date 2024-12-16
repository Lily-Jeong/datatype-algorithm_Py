def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j]<A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step %2d = "%(i+1), A)

data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original: ", data)
selection_sort(data)
print("Selection: ", data)