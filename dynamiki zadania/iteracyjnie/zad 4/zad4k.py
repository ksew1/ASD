from zad4ktesty import runtests

def falisz ( T ):
    W = [[0 for _ in range(len(T))] for _ in range(len(T))]
    for i in range(len(T)):
        W[0][i] = T[0][i] + W[0][i-1]
        W[i][0] = T[i][0] + W[i-1][0]
    for i in range(1, len(T)):
        for j in range(1, len(T)):
            W[i][j] = min(W[i][j-1] + T[i][j], W[i-1][j] + T[i][j])

    return W[len(T)-1][len(T)-1]

runtests ( falisz )
