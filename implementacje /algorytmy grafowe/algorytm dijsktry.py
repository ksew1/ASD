from queue import PriorityQueue
from random import randint

def dijsktra(G, W, s):
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
            if V[v] is False:
                if D[v] > D[u] + W[u][v]:
                    D[v] = D[u] + W[u][v]
                    P[v] = u
                    q.put((D[v],v))
    print(W)
    print(D)

def sol():
    G = [[1, 3], [0, 2], [1, 3], [0, 2]]
    w = [[0 for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(i+1, len(G)):
            w[i][j] = randint(1, 9)
            w[j][i] = w[i][j]
    dijsktra(G, w)

sol()