def move_zeros_to_right(arr):
    pos = 0  # Pointer to track the position for non-zero elements
    
    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:  # If the element is not zero
            # Swap the current element with the element at pos
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1  # Move the pointer to the next position

# Example usage
array = [1, 3, 0, 0, 1, 0, 0, 5]
move_zeros_to_right(array)
print(array)

def move_zeros_to_left(arr):
    pos = len(arr) - 1  # Pointer to track the position for non-zero elements
    
    # Traverse the array from right to left
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:  # If the element is not zero
            # Swap the current element with the element at pos
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -= 1  # Move the pointer to the left

# Example usage
array = [1, 3, 0, 0, 1, 0, 0, 9]
move_zeros_to_left(array)
print(array)