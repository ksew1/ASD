#Karol Sewiło

#O(n^2*p + nlogn)

from zad4testy import runtests
def capacity(tab):
    return (tab[2] - tab[1]) * tab[0]
def select_buildings(T,p):
    tab = sorted(T, key=lambda x: x[2])
    n = len(T)
    F = [[0 for i in range(p+1)] for j in range(n)]
    for b in range(tab[0][3], p+1):
        F[0][b] = capacity(tab[0])
    for b in range(p+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            for k in range(i-1, -1, -1):
                if b - tab[i][3] >= 0 and tab[k][2] < tab[i][1]:
                    F[i][b] = max(F[i][b], F[k][b - tab[i][3]] + capacity(tab[i]))
                    break
            else:
                if b - tab[i][3] >= 0:
                    F[i][b] = max(F[i][b], capacity(tab[i]))

    z = []
    a = p
    i = n -1
    while i > -1 :
        if i == 0 and F[0][a] != 0:
            z.append(tab[0])
        if i != 0 and F[i][a] != F[i-1][a]:
            z.append(tab[i])
            temp = F[i][a]
            a -= tab[i][3]
            cap = capacity(tab[i])
            k = i -1
            for j in range(i-1, -1, -1):

                if F[j][a] + cap == temp:
                    i = k
                    break
                k -= 1
        i -= 1

    w = []
    for i in range(len(z)):
        for j in range(n):
            if z[i] == T[j]:
                w.append(j)

    return w

runtests( select_buildings )