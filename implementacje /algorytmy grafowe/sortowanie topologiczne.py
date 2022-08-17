def DFS(G, L):
    V = [False for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    for u in range(len(G)):
        if not V[u]:
            DFSVisit(G, u, V, P, L)


def DFSVisit(G, u, V, P, L):
    V[u] = True
    for v in G[u]:
        if not V[v]:
            P[v] = u
            DFSVisit(G, v, V, P, L)
    L.append(u)

def top_sort(G):
    L = []
    DFS(G, L)
    L.reverse()
    print(L)


top_sort([[1, 5, 2], [4, 2], [], [], [3, 6], [4], []])

top_sort([[1,2], [], []])