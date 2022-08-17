from zad1testy import Node, runtests


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2


def swap(i, j):
    return j, i


def parent(i):
    return (i-1)//2


def heapify(array, n, i):
    continue_a_loop = True

    while continue_a_loop:
        continue_a_loop = False
        left = left_child(i)
        right = right_child(i)
        max_index = i

        if left < n and array[left].val < array[max_index].val:
            max_index = left
        if right < n and array[right].val < array[max_index].val:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = swap(array[i], array[max_index])
            i = max_index
            continue_a_loop = True


def build_heap(array, n):
    for i in range(parent(n-1), -1, -1):
        heapify(array, n, i)


def append_node(last_node, array):
    last_node.next = array[0]

    return last_node.next


def SortH(p, k):
    n = k + 1
    array = [None for _ in range(n)]

    array[0] = p
    for i in range(1, n):
        p = p.next
        array[i] = p

    if array[n-1] is None:
        n -= 1
    else:
        p = p.next

    build_heap(array, n)

    new_ll = Node()
    last_node = new_ll

    while p is not None:
        last_node = append_node(last_node, array)

        array[0] = p
        p = p.next

        heapify(array, n, 0)

    for i in range(n - 1, 0, -1):
        last_node = append_node(last_node, array)

        array[0] = array[i]
        heapify(array, i, 0)

    # odcinami ostatni węzeł
    last_node.next = array[0]
    last_node = last_node.next
    last_node.next = None

    return new_ll.next


runtests(SortH)
