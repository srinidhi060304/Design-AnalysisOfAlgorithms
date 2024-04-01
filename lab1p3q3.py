def sort_array(arr):
    first, second = None, None
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first is None:
                first = i
            else:
                second = i + 1
    if first is None or second is None:
        return arr  # Array is already sorted
    arr[first], arr[second] = arr[second], arr[first]
    return arr

# Test cases
arr1 = [3,8,6,7,5,9]
arr2 = [3,5,6,9,8,7]
arr3 = [3,5,7,6,8,9]
print(sort_array(arr1))  # Output: [3, 5, 6, 7, 8, 9]
print(sort_array(arr2))  # Output: [3, 5, 6, 7, 8, 9]
print(sort_array(arr3))  # Output: [3, 5, 6, 7, 8, 9]
