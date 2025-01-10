"""
Given an array of size n filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. The task is to find the repetitive element.

Examples:

Input: a[] = {1, 3, 2, 3, 4}
Output: 3
Explanation: The number 3 is the only repeating element.


Input: a[] = {1, 5, 1, 2, 3, 4}
Output: 1

Question:
- Input: sorted ? -> random order, only 1 repeative element, between 1 to N-1
- Output: Return ?
"""

def onlyRepeat(arr):
    # o(n^2)
    # n = len(arr)
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[i] == arr[j]:
    #             return arr[i]
    # return -1
    # o(n)
    set_list = set()
    for num in arr:
        if num in set_list:
            return num
        set_list.add(num)
    return -1


arr = [1,5,1,2,3,4]
onlyRepeat(arr)

