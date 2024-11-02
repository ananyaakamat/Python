def factorial(n):
    """
    Calculate the factorial of a given integer.

    Args:
        n (int): The input number.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    # Ask the user for input
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    # Calculate and display the result
    try:
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()