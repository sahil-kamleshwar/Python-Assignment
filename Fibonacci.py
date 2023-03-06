def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# Take input from the user
n = int(input("Enter the value of n: "))

# Check if the input is valid
if n <= 0:
    print("Invalid input! Please enter a positive integer.")
else:
    print("The", n, "th Fibonacci number is:", fibonacci(n))
