# Karol Sewiło
# Alogrytm bazuje na heapsorcie, tworzymy kolejkę priorytetową długości k + 1 i wpisujemy do niego pierwsze k+1 liczb
# następnie używająć heapify uzyskujemy najmniejszy element który wpinamy do link listy i na jego miejsce w tablicy
# wpisujemy następny element który jest poza tablicą dopóki wszystkie się nie skończą, wtedy sortujemy tablice
# heapsortem a następnie je wpinamy do link listy, którą potem zwracamy

# algorytm ma złożoność nlogk

# k = Θ(1), =  Θ(n)
# k = Θ(logn), =  Θ(nlog^2(n))
# k = Θ(n), =  Θ(nlog(n))

from zad1testy import Node, runtests


def list_to_tab(p):
    tab = []
    while p is not None:
        tab.append(p)
        p = p.next
    return tab


def bubble_sort(tab, k, n):
    for i in range(k):
        for j in range(n - i - 1):
            if tab[j].val > tab[j + 1].val:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


def tab_to_list(tab, n):
    p = tab[0]
    pointer = p
    for i in range(1, n):
        p.next = tab[i]
        p = p.next
    p.next = None
    return pointer


def heapify(tab, n, i):
    changes = True
    while changes:
        changes = False
        left = 2*i + 1
        right = left + 1
        min_id = i
        if left < n and tab[min_id].val > tab[left].val:
            min_id = left
        if right < n and tab[min_id].val > tab[right].val:
            min_id = right
        if min_id != i:
            tab[min_id], tab[i] = tab[i], tab[min_id]
            i = min_id
            changes = True


def build_heap(tab, k):
    for i in range((k-1)//2, -1, -1):
        heapify(tab, k+1, i)


def next_element(tab, p, new_ll, k):
    new_ll.next = tab[0]
    new_ll = new_ll.next
    tab[0] = p
    p = p.next
    heapify(tab, k+1, 0)
    return p, new_ll


def heap_sort(tab, k, new_ll):
    for i in range(k, 0, -1):
        new_ll.next = tab[0]
        new_ll = new_ll.next
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)
    return new_ll


def sorting(p, k):
    tab = [None for _ in range(k + 1)]
    for i in range(k + 1):
        tab[i] = p
        if p is not None:
            p = p.next
    new_ll = Node()
    to_return_ll = new_ll
    if tab[k] is None:
        tab.pop()
        k -= 1
        build_heap(tab, k)
    else:
        build_heap(tab, k)
        while p is not None:
            p, new_ll = next_element(tab, p, new_ll, k)

    new_ll = heap_sort(tab, k, new_ll)
    new_ll.next = tab[0]
    new_ll = new_ll.next
    new_ll.next = None

    return to_return_ll.next


def SortH(p, k):
    if k == 0:
        return p
    if k == 1 or k == 2 or k == 3:
        tab = list_to_tab(p)
        n = len(tab)
        tab = bubble_sort(tab, k, n)
        p = tab_to_list(tab, n)
        return p
    else:
        return sorting(p, k)


runtests( SortH )