def find_second_largest(arr):
    # Initialize variables to store the largest and second largest elements
    largest = second_largest = float('-inf')
    # Iterate through the list and update the largest and second largest elements
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    # Return the second largest element
    return second_largest

# Example usage
arr = [10, 5, 20, 8, 12]
print(find_second_largest(arr)) # Output: 12

arr = [4, 4, 3, 2, 1]
print(find_second_largest(arr)) # Output: 3






