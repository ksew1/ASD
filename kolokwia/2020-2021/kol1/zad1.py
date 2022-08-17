from zad1testy import runtests


def Median(T):
    D = []
    for x in T:
        for y in x:
            D.append(y)
    D.sort()
    a = 0
    b = len(D)-1
    for i in range(len(T)):
        for j in range(len(T)):
            if i < j:
                T[i][j] = D[b]
                b -= 1
            elif i > j:
                T[i][j] = D[a]
                a += 1
    for i in range(len(T)):
        T[i][i] = D[a]
        a += 1

    return T

runtests( Median ) 
