from zad3ktesty import runtests

def ksuma( T, k ):

    W = [-1 for _ in range(len(T))]
    for i in range(k):
        W[i] = T[i]
    for i in range(k, len(T)):
        res = float('inf')
        for j in range(i-k, i):
            res = min(res, W[j])
        W[i] = T[i] + res

    res = float('inf')
    for i in range(len(T)-k, len(T)):
        res = min(W[i], res)
    return res

    
runtests ( ksuma )