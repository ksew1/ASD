def counting_sort(A, k):
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for x in A:
        C[x] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    for i in range(n):
        A[i] = B[i]