def DFS(G, time_proc):
    def DFSVisit(G, u, V, P, time_proc):
        nonlocal time
        V[u] = True
        for v in G[u]:
            if not V[v]:
                P[v] = u
                DFSVisit(G, v, V, P, time_proc)
        time += 1
        time_proc[u] = (u ,time)

    V = [False for _ in range(len(G))]
    P = [None for _ in range(len(G))]

    time = 0
    for u in range(len(G)):
        if not V[u]:
            DFSVisit(G, u, V, P, time_proc)

def DFSrev(rG, time_proc, res):
    def DFSVisit(rG, u, V, P, to_ap):
        V[u] = True
        for v in rG[u]:
            if not V[v]:
                P[v] = u
                DFSVisit(rG, v, V, P, to_ap)
        to_ap.append(u)

    V = [False for _ in range(len(rG))]
    P = [None for _ in range(len(rG))]
    for i in range(len(time_proc)):
        if not V[time_proc[i][0]]:
            to_ap = []
            DFSVisit(rG, time_proc[i][0], V, P, to_ap)
            res.append(to_ap)




def sss(G):
    time_proc = [0 for _ in range(len(G))]
    DFS(G, time_proc)
    time_proc.sort(key=lambda x: x[1], reverse=True)
    rG = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for v in G[i]:
            rG[v].append(i)
    res = []
    DFSrev(rG, time_proc, res)
    print(res)

sss([[1], [2], [], [1]])





