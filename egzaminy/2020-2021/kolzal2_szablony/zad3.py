from zad3testy import runtests
from queue import PriorityQueue
from collections import deque

def dijsktra(G, s):
    D = [float('inf') for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    V = [False for _ in range(len(G))]
    q = PriorityQueue()
    D[s] = 0
    q.put((0, s))
    while q.empty() is False:
        _, u = q.get()
        V[u] = True
        for v in G[u]:
            v, w = v
            if V[v] is False:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    P[v] = u
                    q.put((D[v],v))
    return D, V


def paths(G,s,t):
    Ds, V = dijsktra(G, s)
    if V[t] is False:
        return 0
    Dt, _ = dijsktra(G, t)
    counter = 0
    for i in range(len(G)):
        for x in G[i]:
            if Ds[i] + Dt[x[0]] + x[1] == Ds[t]:
                counter += 1
    return counter

    
runtests( paths )


