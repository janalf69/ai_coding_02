def factorial(n, memo={0: 1, 1: 1}):
    """
    Calculate the factorial of a given number n using memoization.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated

    Returns:
        int: The factorial of the number n
    """
    if n in memo:
        return memo[n]
    else:
        result = n * factorial(n-1, memo)
        memo[n] = result
        return result

def matrix_mult(A, B):
    """
    Multiply two 2x2 matrices.

    Args:
        A (list of lists): The first 2x2 matrix
        B (list of lists): The second 2x2 matrix

    Returns:
        list of lists: The product of the two matrices
    """
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_pow(matrix, n):
    """
    Raise a 2x2 matrix to the power of n using exponentiation by squaring.

    Args:
        matrix (list of lists): The 2x2 matrix
        n (int): The power to which the matrix is raised

    Returns:
        list of lists: The resulting matrix
    """
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        half_power = matrix_pow(matrix, n // 2)
        return matrix_mult(half_power, half_power)
    else:
        return matrix_mult(matrix, matrix_pow(matrix, n - 1))

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation.

    Args:
        n (int): A non-negative integer representing the position in the Fibonacci sequence

    Returns:
        int: The nth Fibonacci number
    """
    if n == 0 or n == 1:
        return n
    
    F = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(F, n - 1)
    
    return result_matrix[0][0]

# Example usage of the function
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")
    print(f"The 10th Fibonacci number is {fibonacci(10)}")
