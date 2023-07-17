def count(arr):
    if not arr:
        return 0
    counter = count(arr[1:])
    return 1 + counter


arr = [0, 1, 2, 3]
print(count(arr))
