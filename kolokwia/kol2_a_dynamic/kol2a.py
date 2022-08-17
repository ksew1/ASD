from kol2atesty import runtests

def f(i, M, S, T):
    if T[i][M] != None:
        return T[i][M]
    if i < 0:
        T[i][M] = float('inf')
        return T[i][M]
    if i == 0 and M == 0:
        T[i][M] = float('inf')
        return T[i][M]
    if i == 0 and M == 1:
        T[i][M] = 0
        return T[i][M]


    if M == 0:
        T[i][M] = min(f(i-1, 1, S, T), f(i-2, 1, S, T), f(i-3, 1, S, T))
        return T[i][M]
    else:
        T[i][M] = min(f(i-1, 0, S, T) + (S[i] - S[i-1]),
                   f(i-2, 0, S, T) + (S[i] - S[i-2]),
                   f(i-3, 0, S, T) + (S[i] - S[i-3]))
        return T[i][M]


def drivers( P, B ):
    W = sorted(P)
    S = [0]
    s = 0
    for x in W:
        if x[1] is True:
            S.append(s + S[-1])
            s = -1
        s += 1
    S.append(s + S[-1])
    T = [[None for i in range(2)] for _ in range(len(S))]

    res = min(f(len(S)-1, 1, S, T), f(len(S)-1, 0, S, T))
    print(res)
    if T[len(S)-1][1] == res:
        M = 1
    else:
        M = 0
    res = []
    i = len(S) -2
    while i > -1:
        if M == 1:
            if i -1 > -1 and T[i-1][0] < T[i-2][0] and T[i-1][0] < T[i-3][0] and (T[i][M] == T[i-1][0] + (S[i] -S[i-1])):
                res.append(S[i])
                res.append(S[i-1])
                i-=1
            elif i -2 > -1 and T[i-2][0] < T[i-1][0] and T[i-2][0] < T[i-3][0] and T[i][M] == T[i-2][0] + (S[i] -S[i-2]):
                res.append(S[i])
                res.append(S[i-2])

                i-=2
            elif i -3 > -1 and T[i-3][0] < T[i-1][0] and T[i-3][0] < T[i-2][0] and T[i][M] == T[i-3][0] + (S[i] -S[i-3]):
                res.append(S[i])
                res.append(S[i-3])
                i -= 3
            M = 0
        else:
            if i -1 > -1 and T[i-1][1] < T[i-2][0] and T[i-1][1] < T[i-3][1] and (T[i][M] == T[i-1][1]):
                i -= 1
            elif i -2 > -1 and T[i-2][1] < T[i-1][1] and T[i-2][1] < T[i-3][1] and (T[i][M] == T[i-2][1]):
                i -= 2
            elif i -3 > -1 and T[i-3][1] < T[i-2][1] and T[i-3][1] < T[i-1][1] and (T[i][M] == T[i-3][1]):
                i -= 3
            else:
                break

            M = 1



    print(res)
    return []










runtests( drivers, all_tests =True )