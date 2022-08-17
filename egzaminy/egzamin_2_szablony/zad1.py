from zad1testy import runtests
from collections import deque

def BFS(G, s):
    V = [False for _ in range(len(G))]
    D = [-1 for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    q = deque()

    D[s] = 0
    V[s] = True
    q.append(s)

    while q:
        u = q.popleft()
        for v in G[u]:
            if not V[v]:
                V[v] = True
                D[v] = D[u] + 1
                P[v] = u
                q.append(v)
    return V


def intuse( I, x, y ):
    Gx = [[] for _ in range(y-x+1)]
    Gy = [[] for _ in range(y-x+1)]
    for el in I:
        if el[0] >= x and el[1] <= y:
            Gx[el[0]-x].append(el[1]-x)
            Gy[el[1]-x].append(el[0]-x)
    Vx = BFS(Gx, 0)
    Vy = BFS(Gy, y-x)
    pass
    res = []
    for i in range(len(I)):
        if I[i][0]-x >= 0 >= I[i][1]-y and Vx[I[i][0] - x] and Vx[I[i][1] - x] and Vy[I[i][0] - x] and Vy[I[i][1] - x]:
            res.append(i)

    return res

    
runtests( intuse )


