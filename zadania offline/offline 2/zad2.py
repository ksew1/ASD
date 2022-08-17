# Karol Sewiło
# Najpierw sortuję podaną listę w kolejności od przedziału którego różnica pomiędzy górnym a dolnym ograniczeniem jest
# największa do tego, którego jest najmniejsza. Tworzę nową listę dla przedziałów i kolejną listę dla liczby
# przedziałów które się w mieszczą w przedziałch w nowej liście. W niej na początku dołączam pierwszy przedział.
# Potem przechodzę kolejnymi przedziałami jeśli nie zawierają się w przedziałach w nowej liście to dodaje
# tam oraz dodaje zero do listy id, jeśli jednak wybrany przedział znajduję się tam to dodaje 1 do listy id pod
# indeksem który odpowiada przedziałowi w którym się zawiera. Na koniec przechodzę po liście indeksów i
# szukam największej wartości a następnie ją zwracam

# złożoność O(nlogn + n)

from zad2testy import runtests


def check_list(new_list, id_list, el):
    flag = True
    for i in range(len(new_list)):
        if new_list[i][1] >= el[1] and new_list[i][0] <= el[0]:
            id_list[i] += 1
            flag = False
    if flag:
        new_list.append(el)
        id_list.append(0)


def partition(tab, p, r):
    x = tab[r][1] - tab[r][0]
    i = p - 1
    for j in range(p, r):
        if tab[j][1] - tab[j][0] >= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i+1


def quicksort_stack(tab, p, r):
    s = [(p, r)]
    while s:
        i, j = s.pop()
        if j > i:
            q = partition(tab, i, j)
            if q - i - 1 < j - q - 1:
                s.append((i, q - 1))
                s.append((q + 1, j))
            else:
                s.append((q + 1, j))
                s.append((i, q - 1))


def depth(L):
    id_list = []
    new_list = []
    quicksort_stack(L, 0, len(L)-1)
    for el in L:
        check_list(new_list, id_list, el)
    max_id = 0
    for ids in id_list:
        max_id = max(max_id, ids)
    return max_id


runtests( depth )
