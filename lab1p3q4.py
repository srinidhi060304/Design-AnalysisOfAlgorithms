def segregate_0_1(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

# Test case
arr = [0,1,0,1,0,0,1,1,1,0]
print(segregate_0_1(arr))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
