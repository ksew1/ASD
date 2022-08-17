from kol3atesty import runtests
from queue import PriorityQueue


def change_E_to_G(E, n):
    G = [[] for _ in range(n)]
    for el in E:
        G[el[0]].append([el[1], el[2]])
        G[el[1]].append([el[0], el[2]])

    return G


def dijsktra(G, a, T, S):
    D = [float('inf') for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    V = [False for _ in range(len(G))]
    q = PriorityQueue()
    D[a] = 0
    q.put((0, a))
    while q.empty() is False:
        _, u = q.get()
        V[u] = True
        for v in G[u]:
            v, w = v
            if V[v] is False:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    P[v] = u
                    if T[v] is True:
                        for x in S:
                            D[x] = D[v]
                            q.put((D[x], x))
                    q.put((D[v],v))
    return D

def spacetravel( n, E, S, a, b ):
    T = [False for _ in range(n)]
    for x in S:
        T[x] = True
    if T[a] and T[b]:
        return 0
    G = change_E_to_G(E, n)
    D = dijsktra(G, a, T, S)

    if D[b] == float('inf'):
        return None
    return D[b]

runtests( spacetravel, all_tests = True)