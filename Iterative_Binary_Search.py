def binary_search_iterative(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# example usage
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_iterative(arr, x)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")