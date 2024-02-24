import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Generate a random array of size 50
random_array = [random.randint(0, 100000) for _ in range(1000)]

# Print the unsorted array
print("Unsorted array:")
print(random_array)

# Measure the time taken to sort the array
start_time = time.time()
bubble_sort(random_array)
end_time = time.time()

# Print the sorted array
print("\nSorted array:")
print(random_array)

# Print the time taken for sorting in milliseconds
print(f"\nTime taken: {(end_time - start_time) * 1000:.6f} milliseconds")
