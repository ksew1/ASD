from zad4ktesty import runtests
def f(x, y, T, W):
    if W[x][y] != -1:
        return W[x][y]
    if x == 0:
        s = 0
        for i in range(y+1):
            s += T[0][i]
        W[x][y] = s
        return W[x][y]
    if y == 0:
        s = 0
        for i in range(x+1):
            s += T[i][0]
        W[x][y] = s
        return W[x][y]

    W[x][y] = min(f(x-1, y, T, W) + T[x][y], f(x, y-1, T, W) + T[x][y])
    return W[x][y]


def falisz ( T ):
    W = [[-1 for _ in range(len(T))] for _ in range(len(T))]
    return f(len(T)-1, len(T)-1, T, W)

runtests ( falisz )
