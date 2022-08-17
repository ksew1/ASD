from kol1atesty import runtests


def syg(s):
    arr = [0 for _ in range(26)]
    for x in s:
        arr[ord(x)-ord('a')] += 1
    return s, arr


def g(T):
    D = []
    for s in T:
        D.append(syg(s))
    D.sort(key=lambda x: (len(x[0]), x[1]))

    counter = 1
    res = 0
    for i in range(len(D)-1):
        if D[i][0] == D[i+1][0] or D[i][0] == D[i+1][0][::-1]:
            counter += 1
        else:
            res = max(res, counter)
            counter = 1



    return res


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
