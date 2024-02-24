def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Sorting
selection_sort(arr)

# Output
print("Sorted array:", arr)