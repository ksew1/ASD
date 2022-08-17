from zad3testy import runtests
from queue import PriorityQueue

# f(i, q) =
def bak(i, j, q, V, T):
    if q - (T[j]-T[i]) + V[j] > q:

        return q
    else:
        return q - (T[j]-T[i]) + V[j]

def f(i, q, T, V, F):
    if i == len(T)-1:
        return 0
    if F[i][q] != -1:
        return F[i][q]

    minx = float('inf')
    j = i + 1
    while j < len(T) and T[j] - T[i] <= q:
        minx = min(minx, f(j, bak(i, j, q, V, T), T, V, F)+1)
        j += 1
    F[i][q] = minx
    return F[i][q]


def iamlate(T, V, q, l):
    T.append(l)
    V.append(0)
    F = [[-1 for _ in range(q+2)] for _ in range(len(T)+2)]
    if V[0] > q:
        print(f(0,q, T, V, F))
    else:    
        print(f(0, V[0], T, V, F))
    return []


runtests( iamlate )
