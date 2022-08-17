# Karol Sewiło

# Algorym polega na zmienieniu reprezentacji krawędziowej na reprezentacje listwą i dodanie do nich krawędzi pomiędzy osobliwościami z wagą 0
# Następnie wykonujemy zwyły algorytm Dijsktry i zwaracamy odlęgość od a do b (jeśli inf to znaczy że nie istnieje taka) zwaracmy None
# Poprawność: Algorytm Dijsktry znajduje najkrótszą szcierzkę a więc i w tym zadaniu powinien dać dobry wynik

from kol3atesty import runtests
from queue import PriorityQueue

# Zwykły algorytm Dijsktry
# nasze liczby są nieujemne czyli rzeczywiste dodatkie czyli wszystko ok bo alg Dijsktry moze byc na takich liczbach
# zero to liczba nieujemna!
# Nie ma pól Parent bo nie są potrzebne do tego zdania

# D - tablica odległości
# V - tablica visited
def dijsktra(G, s):
    D = [float('inf') for _ in range(len(G))] #float('inf') - nieskończność, działa jak inf z math ale nie trzeba importować
    V = [False for _ in range(len(G))]
    q = PriorityQueue()
    D[s] = 0
    q.put((0, s))
    while q.empty() is False:
        _, u = q.get()
        V[u] = True
        for v in G[u]:
            v, w = v
            if V[v] is False: # relaxacjia
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    q.put((D[v],v))
    return D

# Zmeinia nam krawędzie na reprezentacje listową i dodaje krawędzie pomiędzy osonliwościami
# Struktura: G[i] <-- z wiechod i
# w G[i] mamy [el1, el2] z wierzchołka i do el1 z wagą el2
def change_E_to_G(E, n, S):
    G = [[] for _ in range(n)]
    for el in E:
        G[el[0]].append([el[1], el[2]])
        G[el[1]].append([el[0], el[2]])
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i] != S[j]:
                G[S[i]].append([S[j],0])

    return G

# E=m V=n
def spacetravel( n, E, S, a, b ):# średnio mlogn najgorzej n*n
    G = change_E_to_G(E, n, S)
    D = dijsktra(G, a) # O(ElogV)

    if float('inf') == D[b]:
        return None
    return D[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )