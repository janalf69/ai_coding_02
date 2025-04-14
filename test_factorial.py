import unittest
from testing_completion import factorial

class TestFactorial(unittest.TestCase):
    
    def test_base_cases(self):
        """Test the base cases of factorial function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    
    def test_small_numbers(self):
        """Test factorial for small positive integers."""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
    
    def test_larger_number(self):
        """Test factorial for a larger number."""
        self.assertEqual(factorial(10), 3628800)
    
    def test_memoization(self):
        """Test that memoization works correctly."""
        # Clear the memoization dictionary
        memo = {0: 1, 1: 1}
        
        # Calculate factorial(5) and store in memo
        result1 = factorial(5, memo)
        self.assertEqual(result1, 120)
        
        # Verify memo contains the result
        self.assertEqual(memo[5], 120)
        
        # Calculate factorial(5) again using the same memo
        result2 = factorial(5, memo)
        self.assertEqual(result2, 120)

if __name__ == '__main__':
    unittest.main()