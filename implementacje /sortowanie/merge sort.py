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
            if L[i] <= R[j]:
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

