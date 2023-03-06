def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False
    return increasing or decreasing

# Example usage
arr = [1, 2, 3, 4, 5]
print(is_monotonic(arr)) # Output: True

arr = [5, 4, 3, 2, 1]
print(is_monotonic(arr)) # Output: True

arr = [1, 2, 3, 2, 5]
print(is_monotonic(arr)) # Output: False
