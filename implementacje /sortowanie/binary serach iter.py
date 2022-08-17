
def binary_search(arr, x, low, high):

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return True, mid

    return False, high # element powinien być o indeks wyżej



arr = [2, 3, 4, 10, 40]
x = 5

print(binary_search(arr, x, 0, len(arr)-1))


