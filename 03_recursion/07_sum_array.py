def sum_array(arr):
    if not arr:
        return 0
    sum_count = sum_array(arr[1:])
    return arr[0] + sum_count


arr = [3, 5, 2, 5, 7]
print(sum_array(arr))
