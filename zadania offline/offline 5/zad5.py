# Karol Sewiło
# algorytm polega na użyciu kolejki priorytetowej. Na początku zbieramy ropę z pola
# startowego i i przypisujemy go do zmiennej best. Dodajemy do naszej kolejki priorytetowej
# elementy od pola 1 do pola 1 + best. Wyciągamy z kolejki największą wartość i przypisujemy do best i dodajemy
# elementy do kolejki na które mamy teraz zasięg dzięki paliwu z naszego nowego pola best. Powtarzamy te kroki
# aż nasz zasięg będzie równy bądź większy od odległości między miastami
# złożoność kolejki priorytetowej O(logn)
# dodajemy tam n elementów, więc całkowita złożoność to O(nlogn)

from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)
    q = PriorityQueue()

    result = [0]
    a = 1
    b = 1 + T[0]

    while b < n:
        for i in range(a, b):
            if T[i] != 0:
                q.put((-1 * T[i], i))
        best = q.get()
        result.append(best[1])
        a = b
        b += -1 * best[0]

    result.sort()
    return result


runtests( plan, all_tests=True )