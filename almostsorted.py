import sys

def is_sorted(array):
    """
    Check if the given array is sorted in non-decreasing order.

    Args:
    - array (list): The input array.

    Returns:
    - bool: True if the array is sorted, False otherwise.
    """
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))

def almost_sorted(arr):
    """
    Check if the given array can be almost sorted by either swapping two elements or reversing a subarray.

    Args:
    - arr (list): The input array.

    Returns:
    - bool: True if the array can be almost sorted, False otherwise.
    """
    swap_left = -1
    swap_right = -1

    # Find the first occurrence where the array is not sorted.
    for index in range(1, len(arr)):
        if arr[index - 1] > arr[index]:
            swap_left = index - 1
            break
            
    # Find the last occurrence to swap to make the array sorted.
    for index in range(swap_left + 1, len(arr)):
        if index == len(arr) - 1 or arr[index + 1] > arr[swap_left]:
            swap_right = index
            arr[swap_left], arr[swap_right] = arr[swap_right], arr[swap_left]
            break
            
    # Check if the array is sorted after the swap.
    if is_sorted(arr):
        print("yes")
        print("swap {} {}".format(swap_left + 1, swap_right + 1))
        return True
    
    # Undo the swap to explore the next possibility.
    arr[swap_left], arr[swap_right] = arr[swap_right], arr[swap_left]
    
    reverse_left = -1
    reverse_right = -1

    # Find the subarray to reverse to make the array sorted.
    for index in range(len(arr) - 1):
        if reverse_left == -1 and arr[index] > arr[index + 1]:
            reverse_left = index
        elif reverse_left != -1 and arr[index] < arr[index + 1]:
            reverse_right = index
            break
    
    # Reverse the subarray and check if the array is sorted.
    to_reverse = arr[reverse_left:reverse_right + 1]
    arr = arr[:reverse_left] + to_reverse[::-1] + arr[reverse_right + 1:]
    
    if is_sorted(arr):
        print("yes")
        print("reverse {} {}".format(reverse_left + 1, reverse_right + 1))
        return True
    
    # If neither swap nor reverse makes the array sorted.
    print("no")
    return False

if __name__ == "__main__":
    # Read the size of the array.
    array_size = int(input().strip())
    
    # Read the array elements.
    array_elements = list(map(int, input().strip().split(' ')))

    # Check if the array can be almost sorted.
    almost_sorted(array_elements)
