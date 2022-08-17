#Karol Sewiło
# używam bucket sorta aby posortować przedziały

from zad3testy import runtests


def insert_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = key


def bucket_sort(tab, max_el, min_el):
    buckets = [[] for _ in range(len(tab))]
    n = (max_el - min_el) / len(tab)
    for el in tab:
        buckets[int(el / n) + 1].append(el)
    new_list = []
    for el in buckets:
        insert_sort(el)
        new_list.extend(el)
    return new_list


def SortTab(T, P):
    max_el = 0
    min_el = float('inf')
    for el in P:
        max_el = max(max_el, el[1])
        min_el = min(min_el, el[0])
    T = bucket_sort(T, max_el, min_el)

    return T


runtests( SortTab )