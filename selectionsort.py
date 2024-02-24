import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Generate a random array of size 1000
random_array = [random.randint(0, 10000) for _ in range(1000)]

# Measure the time taken for sorting
start_time = time.time()
selection_sort(random_array)
end_time = time.time()

# Calculate the time taken in milliseconds
time_taken_ms = (end_time - start_time) * 1000

print("Sorted Array:", random_array)
print("Time taken for sorting:", time_taken_ms, "milliseconds")
