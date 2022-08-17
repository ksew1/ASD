
def binary_search(arr, x, low, high):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return True, mid

        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)

        else:
            return binary_search(arr, x, mid + 1, high)
    else:
        return False, high


arr = [ 2, 3, 4, 10, 40 ]
x = 1

print(binary_search(arr, x, 0, len(arr)-1))
