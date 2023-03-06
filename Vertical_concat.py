import numpy as np

# create two arrays to concatenate vertically
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# perform vertical concatenation
result = np.vstack((arr1, arr2))

print("Original arrays:")
print(arr1)
print(arr2)

print("\nResult of vertical concatenation:")
print(result)