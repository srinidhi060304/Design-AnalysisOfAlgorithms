import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random array of size 50
random_array = [random.randint(0, 100000) for _ in range(1000)]

# Measure the time taken for sorting
start_time = time.time()
insertion_sort(random_array)
end_time = time.time()

# Calculate the time taken in milliseconds
execution_time_ms = (end_time - start_time) * 1000

print("Sorted array:", random_array)
print("Time taken for sorting: {:.6f} milliseconds".format(execution_time_ms))
