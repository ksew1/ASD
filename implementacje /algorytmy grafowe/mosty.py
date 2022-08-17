def DFS(G):
    def DFSVisit(G, u, T, low):
        nonlocal time
        time += 1
        V[u] = True

        T[u] = time
        low[u] = time
        for v in G[u]:
            if V[v] is False:
                P[v] = u
                DFSVisit(G, v, T, low)
            else:
                if v != P[u]:
                    low[u] = min(low[u], low[v])
        for v in G[u]:
            if v != P[u]:
                low[u] = min(low[u], low[v])

    V = [False for _ in range(len(G))]
    P = [None for _ in range(len(G))]
    T = [0 for _ in range(len(G))]
    low = [float('inf') for _ in range(len(G))]

    time = 0
    DFSVisit(G, 0, T, low)
    return low, T, P

def main(G):
    low, T, P = DFS(G)
    for i in range(len(low)):
        if T[i] == low[i]:
            if P[i] != None:
                print( "E (", P[i], i, ")")

main([[1, 6], [0, 2], [1, 3, 6], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]])