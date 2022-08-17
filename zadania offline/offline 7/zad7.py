# Karol Sewiło

# Do rozwiązania używam DFSa przechodzę od wierzchołka 0 i dodaje go do listy, jeśli trafie w ślepy zaułek
# usuwam ostatni dodany wierzchołek jeśli znajdę cykl od długości grafu i który kończy się na zero to zawracam True
# i zakańczam rekurencje zwracając tablice z wierzchołkami
# złożoność pesymistyczna O(n!)


from zad7testy import runtests


def DFS(G):
    base = ((0, 1), (1, 0))
    n = len(G)
    for el in base:
        V = [False for _ in range(n)]
        P = [None for _ in range(n)]
        D = [0 for _ in range(n)]
        t = []
        DFSVisit(G, 0, V, P, D, t, el)
        if len(t) == len(G):
            return t
    return None


def DFSVisit(G, u, V, P, D, res, base):
    V[u] = True
    mark = base[0]
    res.append(u)
    if P[u] in G[u][mark]:
        mark = base[1]
    if D[u] + 1 == len(G) and 0 in G[u][mark]:
        return True
    for v in G[u][mark]:
        if V[v] is False:
            D[v] = D[u] + 1
            P[v] = u
            if DFSVisit(G, v, V, P, D, res, base):
                return True
    res.pop()
    V[u] = False
    return False


def droga(G):
    return DFS(G)


runtests( droga, all_tests = True)
