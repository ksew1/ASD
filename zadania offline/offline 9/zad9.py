# Karol Sewiło

# Algorytm to brute force, który opiera się na metodzie Forda-Fulkersona. Wywołujemy ją dla każdej pary
# wierzchołków i zwracamy dla największej wartości. Mamy 2 dodatkowe warunki które służą optymalizacji.
# Funkcja sum_of_drain oblicza wagę krawędzi, które wchodzą do naszych 2 wierzchołków. Jeśli nasza para ma
# sumę mniejszą niż nasz bieżący najwyższy wynik to nie wykonujemy metody ponieważ wynik i tak będzie mniejszy
# Kolejny warunek jest podobny, liczymy sumę krawędzi wychodzących ze źródła i jeśli jakaś para osiągnie tą wartość
# to kończymy pętle i zwracamy ten wynik ponieważ jest on najlepszy jaki jest możliwy
# złożoność O(V^3*E^2)

from zad9testy import runtests
from collections import deque


def call_flow(M, w, P, suma):
    res = float('inf')
    v = w
    while P[v] is not None:
        res = min(res, M[P[v]][v])
        v = P[v]
    v = w
    while P[v] is not None:
        M[P[v]][v] -= res
        M[v][P[v]] += res
        v = P[v]

    suma[0] += res
    return


def BFS(M, s, t1, t2, suma):
    q = deque()
    V = [False for _ in range(len(M))]
    P = [None for _ in range(len(M))]
    V[s] = True
    q.append(s)
    while q:
        u = q.popleft()
        for v in range(len(M)):
            if M[u][v] != 0 and not V[v] and (v == t1 or v == t2):
                P[v] = u
                call_flow(M, v, P, suma)
                return True
            if M[u][v] != 0 and not V[v]:
                V[v] = True
                P[v] = u
                q.append(v)
    return False


def make_arr(G):
    n = len(G)
    M = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for el in G:
        M[el[0]][el[1]] = el[2]
    return M


def sum_of_drain(t1, t2, G):
    sum_drain = 0
    for el in G:
        if el[1] == t1 or el[1] == t2:
            sum_drain += el[2]
    return sum_drain


def maxflow(G, s):
    n = len(G)
    final_sum = 0
    max_flow = 0
    for el in G:
        if el[0] == s:
            max_flow += el[2]

    for t1 in range(1, n + 1):
        for t2 in range(t1 + 1, n + 1):
            flag = True
            suma = [0]
            M = make_arr(G)
            sum_drain = sum_of_drain(t1, t2, G)
            if sum_drain > final_sum:
                while flag:
                    flag = BFS(M, s, t1, t2, suma)
                final_sum = max(final_sum, suma[0])

                if final_sum == max_flow:
                    return final_sum

    return final_sum


runtests(maxflow, all_tests=True)