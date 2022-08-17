from kol1btesty import runtests


def syg(s):
    arr = [0 for _ in range(26)]
    for x in s:
        arr[ord(x)-ord('a')] += 1
    arr = tuple(arr)
    return len(s), arr


def check_syg(a, b):
    for i in range(26):
        if a[i] != b[i]:
            return False
    return True


def counting_sort(A, key):
    n = len(A)
    k = -1
    for i in range(n):
        k = max(k, A[i][1][key])

    C = [0 for _ in range(k+1)]
    B = [0 for _ in range(n)]

    for i in range(n):
        x = A[i][1][key]
        C[x] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(n - 1, -1, -1):
        idx = A[i][1][key]
        B[C[idx]-1] = A[i]
        C[idx] -= 1
    for i in range(n):
        A[i] = B[i]
    return A

def counting_sortv2(A):
    n = len(A)
    k = -1
    for i in range(n):
        k = max(k, A[i][0])
    C = [0 for _ in range(k+1)]
    B = [0 for _ in range(n)]

    for i in range(n):
        x = A[i][0]
        C[x] += 1

    for i in range(1, k+1):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i][0]]-1] = A[i]
        C[A[i][0]] -= 1

    for i in range(n):
        A[i] = B[i]
        
def radix_sort(D):
    for i in range(25, -1, -1):
        D = counting_sort(D, i)
    counting_sortv2(D)

def f(T):
    D = []
    for s in T:
        D.append(syg(s))
    radix_sort(D)

    counter = 1
    res = 1
    for i in range(len(D)-1):
        if check_syg(D[i][1], D[i+1][1]):
            counter += 1
        else:
            res = max(res, counter)
            counter = 1
    res = max(res, counter)
    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
