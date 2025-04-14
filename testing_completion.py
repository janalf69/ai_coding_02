def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): A non-negative integer representing the position in the Fibonacci sequence

    Returns:
        int: The nth Fibonacci number
    """
    result = 0
    a, b = 0, 1
    for i in range(n):
        result = a + b
        a, b = b, result
        print(f'fib({i}) = {result}')
    return result

print(fibonacci(10))

def factorial(n):
    """
    Calculate the factorial of a given number n.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated

    Returns:
        int: The factorial of the number n
    """
    if n == 0:
        return 1  # Factorial of 0 is 1, not 0
    elif n == 1:
        return 1  # Factorial of 1 is 1
    else:
        result = n * factorial(n-1)
        return result

# Example usage of the function
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")
