def binary_search_recursive(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search_recursive(arr, x, low, mid - 1)
    else:
        return binary_search_recursive(arr, x, mid + 1, high)

# example usage
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_recursive(arr, x, 0, len(arr) - 1)
if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")