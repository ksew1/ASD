from zad3ktesty import runtests

def f(a, k, T, W):
    if W[a] is not None:
        return W[a]
    if a - k < 0:
        W[a] = 0
        return W[a]
    res = float('inf')
    for i in range(a-k, a):
        res = min(f(i, k, T, W) + T[i], res)
    W[a] = res
    return W[a]


def ksuma(T, k):
    W = [None for _ in range(len(T)+1)]
    return f(len(T), k, T, W)
    
runtests (ksuma)