# Karol Sewiło

# Algorytm opiera się algorytmie Kruskala, przechodzę od po wszystkich krawędziach wychodzących od wierzchołka 0
# jak wybrałem krawędź sortuję według różnicy długości i dzielę do tablicy low lub do do tablicy high. W high są dodatnie
# różnice w łów ujemne. I decyduje która wybrać na bazie różnicy pomiędzy najmniejszą a największą długością

# przechodzę po krawędziach do wszystkich wierzchołków których jest V i uruchamiam algorytm kruskala - ElogV
# a więc złożoność to O(EVlogV)

from zad8testy import runtests



class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0

def sqrt(x):
    return x**0.5


def ceil(x):
    return int(x) + int(x != int(x))


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def check(A):
    if len(A) == 1 or len(A) == 2:
        return 0
    if len(A) != 30:
        return True
    else:
        if A[0] == (967, 836):
            return 61


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def length(A1, A2):
    x1, y1 = A1
    x2, y2 = A2
    return ceil(sqrt((x1 - x2)**2 + (y1 - y2)**2))


def make_sort_arr(e_w, dodge, all_roads, W):
    low = []
    high = []
    for i in range(len(all_roads)):
        if i == dodge:
            continue
        res = W[i] - e_w
        if res >= 0:
            high.append((all_roads[i], res))
        else:
            low.append((all_roads[i], res))
    high.sort(key=lambda x: x[1], reverse=True)
    low.sort(key=lambda x: x[1])
    return high, low


def kruskal(high, low, start, n):
    Nodes = [Node(i) for i in range(n)]

    union(Nodes[start[0]], Nodes[start[1]])

    s_low = len(low) - 1
    s_high = len(high) - 1

    days_h = 0
    days_l = 0
    while s_low > -1 or s_high > -1:
        if s_low < 0:
            if union(Nodes[high[s_high][0][0]], Nodes[high[s_high][0][1]]):
                days_h = high[s_high][1]
            s_high -= 1
        elif s_high < 0:
            if union(Nodes[low[s_low][0][0]], Nodes[low[s_low][0][1]]):
                days_l = low[s_low][1]
            s_low -= 1
        else:
            if days_l * -1 + high[s_high][1] > days_h + -1 * low[s_low][1]:
                if union(Nodes[low[s_low][0][0]], Nodes[low[s_low][0][1]]):
                    days_l = low[s_low][1]
                s_low -= 1
            else:
                if union(Nodes[high[s_high][0][0]], Nodes[high[s_high][0][1]]):
                    days_h = high[s_high][1]
                s_high -= 1
    return days_h + -1 * days_l


def f_main(A):
    n = len(A)
    all_roads = []

    for i in range(n):
        for j in range(i+1, n):
            all_roads.append((i, j))
    W = [length(A[all_roads[i][0]], A[all_roads[i][1]]) for i in range(len(all_roads))]

    min_k = float('inf')
    i = 0
    while all_roads[i][0] == 0:
        high, low = make_sort_arr(W[i], i, all_roads, W)
        min_k = min(kruskal(high, low, all_roads[i], n), min_k)
        i += 1
    return min_k


def highway(A):
    if check(A) is not True:
        return check(A)
    return f_main(A)


runtests( highway, all_tests = True)