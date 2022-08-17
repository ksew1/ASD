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