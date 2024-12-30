"""
Given an array arr[] of size N, find the prefix sum of the array. 
A prefix sum array is another array prefixSum[] of the same size, 
such that the value of prefixSum[i] is arr[0] + arr[1] + arr[2] . . . arr[i].

Examples: 

Input: arr[] = {10, 20, 10, 5, 15}
Output: prefixSum[] = {10, 30, 40, 45, 60}
Explanation: While traversing the array, update the element by adding it with its previous element.
prefixSum[0] = 10, 
prefixSum[1] = prefixSum[0] + arr[1] = 30, 
prefixSum[2] = prefixSum[1] + arr[2] = 40 and so on.
"""

def prefix_sum_array(arr):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for i in range(1, len(arr)):
        prefix_sum.append(prefix_sum[i-1] + arr[i])
    return prefix_sum

arr = [10, 20, 10, 5, 15]
print(prefix_sum_array(arr))
