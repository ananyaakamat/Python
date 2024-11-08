# Function to find the next Fibonacci number after the given number
def next_fibonacci(n):
    # If the input number is less than or equal to 0, return 0
    if n <= 0:
        return 0
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Loop until the next Fibonacci number is greater than the input number
    while b <= n:
        # Update the values of a and b to the next two Fibonacci numbers
        a, b = b, a + b
    
    # Return the next Fibonacci number
    return b

# Ask the user to input a number
input_number = int(input("Enter a number: "))

# Print the next Fibonacci number after the input number
print(next_fibonacci(input_number))