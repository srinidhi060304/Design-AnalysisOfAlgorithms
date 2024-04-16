def maximize_sum(arr):
    arr.sort()  # Sort the array

    max_sum = sum(arr[i] * i for i in range(len(arr)))
    return max_sum

# Example usage
arr = [2, 5, 3, 4, 0]
maximized_sum = maximize_sum(arr)
print("Maximized sum:", maximized_sum)
