"""
Given an unsorted array of size n. Array elements are in the range of 1 to n. 
One number from set {1, 2, …n} is missing and one number occurs twice in the array. 
Find these two numbers.

Examples: 

Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1


Question-driven:
Input Constraints:
- sort or unsort ?
- interger ?
- Exactly one number in the array is missing.
- Exactly one number occurs twice in the array.
Output Requirements:
- Return the missing number and the repeating number as a pair (Missing, Repeating)
Edge Cases:
- the minimum valid size 
"""

def missingRepeat(arr):
    n = len(arr)
    freq = [0] * (n+1)
    # Count occurrences of each number in the array
    for num in arr:
        freq[num] += 1
    # Identify the repeating and missing numbers
    repeating = missing = -1
    for i in range(1, n + 1):
        if freq[i] == 2:  # Number appears twice
            repeating = i
        elif freq[i] == 0: # Number is missing
            missing = i
    return (missing, repeating)

arr = [7, 3, 4, 5, 5, 6, 2]
missingRepeat(arr)
