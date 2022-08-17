from zad1ktesty import runtests

def count(b, S):
    if S[b] == '0':
        return 1
    else:
        return -1
def roznica( S ):
    n = len(S)
    T = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if S[i] == '0':
            T[i][i] = 1

    for a in range(n):
        for b in range(a+1, n):
            T[a][b] = T[a][b-1] + count(b, S)
    res = -1
    for x in T:
        res = max(res, max(x))


    return res

runtests ( roznica )