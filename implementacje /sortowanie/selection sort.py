def selection_sort(T): #  test 2 (do test 2)   2.77 sekund
    n = len(T)
    for i in range(n):
        low = i
        for j in range(i+1, n):
            if T[j] < T[low]:
                low = j
        T[i], T[low] = T[low], T[i]
