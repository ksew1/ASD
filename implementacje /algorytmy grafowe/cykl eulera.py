def euler(G):

    for u in G:
        if len(u) % 2 != 0:
            return 0
    M = [[False for _ in range(len(G))] for _ in range(len(G))]

    for u in range(len(G)):
        for v in G[u]:
            M[u][v] = True

    L = []
    DFS(G, M, L)
    L.reverse()
    print(L)
    return 1


def DFS(G, M, L):
    last_id = [0 for _ in range(len(G))]
    DFSVisit(G, 0, M, L, last_id)


def DFSVisit(G, u, M, L, last_id):
    for i in range(last_id[u], len(G[u])):
        last_id[u] = i
        v = G[u][i]
        if M[u][v] is True:
            M[u][v] = False
            M[v][u] = False
            DFSVisit(G, v, M, L, last_id)
    L.append(u)


#euler([[1, 2], [0, 2], [0, 1]])
euler([[1, 2], [0, 2, 3, 4], [0, 3, 1, 4], [1, 2, 4, 5], [3, 5, 1, 2], [3, 4]])