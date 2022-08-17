def insertion_sort(T): #  test 2 (do test 2)  2.84 sekund
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
