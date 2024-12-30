"""
Given an array arr[], sort the array according to the following relations:  

arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
Find the resultant array.[consider 1-based indexing]

Examples:  

Input: arr[] = [1, 2, 2, 1]
Output: [1 2 1 2]
 Explanation:
For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.
"""

def rearrangeArray(arr):
    n = len(arr)
    for i in range(1, n):
        # (i+1) is the 1-based index
        if (i + 1) % 2 == 0:
            # Even index in 1-based => arr[i] >= arr[i-1]
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        else:
            # Odd index in 1-based => arr[i] <= arr[i-1]
            if arr[i] > arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr
    

arr = [1, 2, 2, 1]
res = rearrangeArray(arr)
print(res)


import unittest
class TestRearrangeArray(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(rearrangeArray([1, -2, 3, -4, 5, -6]), [1, -2, 3, -4, 5, -6])
        self.assertEqual(rearrangeArray([-1, 2, -3, 4, -5, 6]), [-1, 2, -3, 4, -5, 6])
    
    def test_all_positive(self):
        self.assertEqual(rearrangeArray([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_all_negative(self):
        self.assertEqual(rearrangeArray([-1, -2, -3, -4, -5]), [-1, -2, -3, -4, -5])
    
    def test_empty_array(self):
        self.assertEqual(rearrangeArray([]), [])
    
    def test_single_element(self):
        self.assertEqual(rearrangeArray([1]), [1])
        self.assertEqual(rearrangeArray([-1]), [-1])
    
    def test_alternating_numbers(self):
        self.assertEqual(rearrangeArray([1, -1, 2, -2, 3, -3]), [1, -1, 2, -2, 3, -3])
        self.assertEqual(rearrangeArray([-1, 1, -2, 2, -3, 3]), [-1, 1, -2, 2, -3, 3])

if __name__ == '__main__':
    unittest.main()