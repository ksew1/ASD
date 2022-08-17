# Karol Sewiło

from kolutesty import runtests

# podany algorytm to algorytm zachłany. Jako, że liczy się tylko zmiana dyskietki, to póki
# jest to możliwe instalujemy pliki z niej.  Ponieważ nic nas to nie kosztuje. Jeśli jest to jednak
# nie możliwe to zmieniamy dyskietkę i powtażamy aż nie zainstalujemy wsztystkich plików
# jeśli udało by się na zrobić usuwanie w czasie stałym i sprawdzanie czy w logn to mamy nlogn
# niestety zabrakło mi czasu

def possible(L, R): # funkcja sprawdzająca czy jest możliwe zainstalowanie L
    for x in L:
        if not R[x]:
            return False
    return True


def f(letter, disk, depends, A, B):
    s = 0
    V = [False for _ in range(len(disk))] # czy plik i został zainstalowany
    len_V = 0 # ilość wartości True
    while len_V < len(disk): # wysztkie pliki odwiedzone jeśli False
        changes = False
        if letter == 'A': # używamy tablica A czy tablicy B
            T = A
        else:
            T = B
        for x in T:
            if not V[x]:
                if len_V >= len(depends[x]) and possible(depends[x], V):
                    len_V += 1
                    V[x] = True
                    changes = True
        if changes is False: # nie da się wicej dodać z wybranej dyskietki, trzeba zmienić na przeciwną
            s += 1
            if letter == 'A':
                letter = 'B'
            else:
                letter = 'A'

    return s






def swaps( disk, depends ):
    A = [] # # tablica z indeskami dyskietek a
    for i in range(len(disk)):
        if disk[i] == 'A':
            A.append(i)
    B = [] # tablica z indeskami dyskietek b
    for i in range(len(disk)):
        if disk[i] == 'B':
            B.append(i)
    res = min(f('A', disk, depends, A, B), f('B', disk, depends, A, B))

    return res


runtests( swaps, all_tests = True )

