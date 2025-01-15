"""
Given an integer array arr[], print all distinct elements from this array. 
The given array may contain duplicates and the output should contain every element only once.

Examples: 

Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
Output: {12, 10, 9, 45, 2}


Input: arr[] = {1, 2, 3, 4, 5}
Output: {1, 2, 3, 4, 5}


Input: arr[] = {1, 1, 1, 1, 1}
Output: {1}
"""

def findDistinct(arr):
    # brute-force
    arr.sort()
    for i in range(len(arr)):
        # Store elements only if they are different 
        # from previous element
        if i == 0 or arr[i] != arr[i - 1]:
            res.append(arr[i])
    # using tuple for deduplicate: T: O(1), S: O(n)
    print("Debug")
    print("Tupple: ", set(arr))
    return set(arr)


if __name__ == "__main__":
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    res = findDistinct(arr)
    for val in res:
        print(val, end=" ")