from zad1testy import runtests

"""def binary_search(arr, x, low, high):

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return high # element powinien być o indeks wyżej

def chaos_index( T ):
    flag = False
    for i in range(len(T)-1):
        if T[i] != T[i+1]:
            flag = True
    if flag is False:
        return 0
    D = sorted(T)
    res = -1
    W = {}
    for i in range(len(T)):
        x = binary_search(D, T[i], 0, len(T)-1)
        res = max(res, abs(x-i))
        W.update({T[i]: min(T[i], res)})
    res2 = -1
    for x in W.values():
        res2 = max(res2, x)

    return min(res, res2)
"""
def merge_sort(T): # test 2 (wszystko) 8.9 sek
    if len(T) > 1:
        p = len(T)//2
        L = T[:p]
        R = T[p:]
        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1

def chaos_index( T ):
    D = []
    for i in range(len(T)):
        D.append((T[i], i))
    merge_sort(D)
    print(D)
    res = -1
    for i in range(len(D)):
        res = max(res, abs(i-D[i][1]))

    return res



runtests( chaos_index )
