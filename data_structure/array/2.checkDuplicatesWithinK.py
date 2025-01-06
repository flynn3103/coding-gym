"""
Given an unsorted array that may contain duplicates. 
Also given a number k which is smaller than the size of the array. 
Write a function that returns true if the array contains duplicates within k distance.
Examples: 

Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
Output: false
All duplicates are more than k distance away.

Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
Output: true
1 is repeated at distance 3.

Input: k = 3, arr[] = {1, 2, 3, 4, 5}
Output: false

Input: k = 3, arr[] = {1, 2, 3, 4, 4}
Output: true
"""

def checkDuplicatesWithinK(arr, k):
    n = len(arr)
    # brute force
    # for i in range(n):
    #     for j in range(i + 1, min(i + k + 1, n)):
    #         if arr[i] == arr[j]:
    #             return True
    # return False
    # Time complexity: O(n^2)
    # Optimized solution
    window = set()
    # check duplicate 
    for i, val in enumerate(arr):
        if val in window:
            return True
        window.add(val)
        if len(window) > k:
            window.remove(arr[i - k])
    return False

# Driver method to test above method
arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if checkDuplicatesWithinK(arr, 3) else "No")


import unittest

class TestCheckDuplicatesWithinK(unittest.TestCase):
    def test_duplicates_within_k(self):
        self.assertTrue(checkDuplicatesWithinK([1, 2, 3, 1, 4, 5], 3))
    
    def test_duplicates_not_within_k(self):
        self.assertFalse(checkDuplicatesWithinK([1, 2, 3, 4, 1, 2, 3, 4], 3))
    
    def test_no_duplicates(self):
        self.assertFalse(checkDuplicatesWithinK([1, 2, 3, 4, 5], 3))
    
    def test_empty_array(self):
        self.assertFalse(checkDuplicatesWithinK([], 3))
    
    def test_single_element_array(self):
        self.assertFalse(checkDuplicatesWithinK([1], 3))
    
    def test_multiple_duplicates_within_k(self):
        self.assertTrue(checkDuplicatesWithinK([1, 2, 3, 4, 4], 3))

if __name__ == '__main__':
    unittest.main()
