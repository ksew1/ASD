from zad2ktesty import runtests

def f(a, b, S, T):
    if T[a][b] is not None:
        return T[a][b]
    if a == b:
        T[a][b] = True
        return T[a][b]
    if a + 1 == b and S[a] == S[b]:
        T[a][b] = True
        return T[a][b]
    if S[a] == S[b]:
        T[a][b] = f(a+1, b-1, S, T)
        return T[a][b]
    T[a][b] = False
    return T[a][b]

def palindrom( S ):
    T = [[None for _ in range(len(S))] for _ in range(len(S))]
    for a in range(len(S)):
        for b in range(a+1, len(S)):
            f(a, b, S, T)

    max_l = (0, 1)
    for a in range(len(S)):
        for b in range(len(S)):
            if T[a][b] is True and b - a > max_l[1] - max_l[0]:
                max_l = (a, b)

    return S[max_l[0]:max_l[1]+1]


runtests ( palindrom )