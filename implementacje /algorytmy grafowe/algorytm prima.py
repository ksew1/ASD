from queue import PriorityQueue

def prim(G, w):
    V = [False for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    W = [float('inf') for _ in range(len(G))]

    W[0] = 0
    q = PriorityQueue()
    q.put((0,0))
    while q.empty() is False:
        _, t = q.get()
        V[t] = True
        for u in G[t]:
            if V[u] is False:
                if W[u] >= w[t][u]:
                    W[u] = w[t][u]
                    P[u] = t
                    q.put((W[u],u))
    print(W)
    print(P)

    
def sol():
    G = [[1, 3], [0, 2], [1, 3], [0, 2]]
    w = [[0 for _ in range(len(G))] for _ in range(len(G))]
    w[0][1] = 3
    w[1][0] = 3
    w[1][2] = 4
    w[2][1] = 4
    w[2][3] = 100
    w[3][2] = 100
    w[3][0] = 1
    w[0][3] = 1
    prim(G, w)



sol()
