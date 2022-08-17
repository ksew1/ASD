from zad1ktesty import runtests


def count(b, S):
    if S[b] == '0':
        return 1
    else:
        return -1


def f(a, b, S, T):
    if T[a][b] is not None:
        return T[a][b]
    if a == b:
        if S[a] == '0':
            return 1
        else:
            return -1
    T[a][b] = f(a, b - 1, S, T) + count(b, S)
    return T[a][b]


def roznica( S ):
    res = -1
    T = [[None for _ in range(len(S))] for _ in range(len(S))]
    for a in range(len(S)):
        for b in range(a+1, len(S)):
            res = max(res, f(a, b, S, T))

    return res


runtests ( roznica )