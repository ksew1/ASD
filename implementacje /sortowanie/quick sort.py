def quick_sort(A, p, r): # test 2 (wszystko) 5.5 sek interacyjny trochę szypciej
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def quick_sort_stack(A, p, r):
    S = [(p, r)]
    while S:
        i, j = S.pop()
        if j > i:
            q = partition(A, i, j)
            S.append((i, q - 1))
            S.append((q + 1, j))


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1




