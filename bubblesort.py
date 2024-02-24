def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in this pass
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break

arr = input("Enter the array elements separated by spaces: ").split()
# Convert input strings to integers
arr = [int(num) for num in arr]

# Call bubble_sort function
bubble_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
