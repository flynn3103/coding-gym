def binary_search(arr, target):
    """
    Perform a binary search to find the target in a sorted array.

    Parameters:
    arr (list): A list of sorted elements.
    target (int/float): The element to search for in the array.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in array")