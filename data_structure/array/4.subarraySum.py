"""
Given an integer array arr[], find the sum of all sub-arrays of the given array. 

Examples: 

Input: arr[] = [1, 2, 3]
Output: 20
Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20


Input: arr[] = [1, 2, 3, 4]
Output: 50

"""

def sumOfSubarrays(arr):
    n = len(arr)
    total_sum = 0
    # Pick starting point
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            total_sum += curr_sum

    return total_sum


def sumOfSubarrays(arr):
    """
    The optimized solution uses a mathematical observation: 
    each element contributes to multiple subarrays based on its position.
    For array [1, 2, 3]:

    Element 1 appears in: [1], [1,2], [1,2,3]
    Element 2 appears in: [2], [2,3], [1,2], [1,2,3]
    Element 3 appears in: [3], [2,3], [1,2,3]
    """

    n = len(arr)
    total = 0
    for i in range(n):
        total += arr[i] * (i + 1) * (n - i)
    return total

import unittest

class TestArraySum(unittest.TestCase):
    def test_sumOfSubarrays(self):
        self.assertEqual(sumOfSubarrays([1, 2, 3]), 20)
        self.assertEqual(sumOfSubarrays([1, 2, 3, 4]), 50)
        self.assertEqual(sumOfSubarrays([5]), 5)
        self.assertEqual(sumOfSubarrays([]), 0)
        self.assertEqual(sumOfSubarrays([-1, -2]), -6)
    
    def test_large_array(self):
        arr = list(range(1, 101))
        self.assertTrue(sumOfSubarrays(arr) > 0)
       
    def test_input_validation(self):
        with self.assertRaises(TypeError):
            sumOfSubarrays(None)
        with self.assertRaises(TypeError):
            sumOfSubarrays("123")
    
    def test_duplicates_and_unsorted(self):
        self.assertEqual(sumOfSubarrays([3, 1, 3]), 22)  # Same result as [1, 2, 3]
        self.assertEqual(sumOfSubarrays([2, 2, 2]), 20)  # All duplicates
        self.assertEqual(sumOfSubarrays([4, 1, 2]), 22)  # Unsorted
    
if __name__ == '__main__':
   unittest.main()