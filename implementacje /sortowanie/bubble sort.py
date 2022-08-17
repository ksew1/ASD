def bubble_sort(T):   # test 2 6.49 (do test 2) sekund
    n = len(T) - 1

    for i in range(n):

        flag = True

        for j in range(n-i):

            if T[j] > T[j+1]:
                flag = False
                T[j], T[j+1] = T[j+1], T[j]

        if flag:
            return T

    return T
