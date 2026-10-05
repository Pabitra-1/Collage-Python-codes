def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(arr, 0, len(arr) - 1, target)

print("Index:", result)