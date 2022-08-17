# Karol Sewiło

# Algorytm polega na dwukrotnym użyciu BFSa. Za pierwszym razem przechodzimy nim po całym grafie z s,
# nie dodając wierzchołka t
# (wynik powinien być ten sam co z dodawaniem wierzchołka t ale nie moglibyśmy znaleźć jak przebiega dłuższa ścieżka,
# ponieważ parent punktu dłuższej ścieżki wskazywał by na t) następnie sprawdzamy wszystkich sąsiadów wierzchołka t i
# dodajemy do kolejki tylko tych co mają najmniejszą długość (którą wcześniej wyznaczam).
# Jeśli w kolejce jest tylko 1  element to znaczy że jest tylko jedna taka ścieżka, a więc wystarczy usunąć
# krawędź, która łączy ją z punktem t. Jeśli jest więcej ścieżek to musimy je przebadać BFSem i sprawdzić kiedy się
# łączą w jedną, więc kolejka ma długość 1 i usuwamy punkt gdzie się złączyły
# używamy 2 krotnie BFSa, a więc złożoność to O(V+E)

from zad6testy import runtests
from collections import deque


def bfs(G, q, d, parent):
    n = len(G)
    visited = [False for _ in range(n)]

    while len(q) > 1:
        u = q.popleft()
        for v in G[u]:
            if v is not None and not visited[v] and d[v] == d[u] - 1:
                visited[v] = True
                q.append(v)
    if parent[q[0]] is None:
        return None
    else:
        return parent[q[0]], q[0]


def longer(G, s, t):
    n = len(G)
    d = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    q = deque()
    visited[s] = True
    q.append(s)
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                if v != t:
                    q.append(v)

    low = float('inf')
    for el in G[t]:
        low = min(d[el], low)

    lows = deque()
    for el in G[t]:
        if d[el] == low:
            lows.append(el)

    if len(lows) > 1:
        return bfs(G, lows, d, parent)
    else:
        if lows[0] is None:
            return None
        else:
            return lows[0], t


runtests(longer, all_tests=True)
