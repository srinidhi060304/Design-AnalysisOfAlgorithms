import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate random numbers
numbers = [random.randint(1, 10000) for _ in range(1000)]

# Measure time for bubble sort
start_time = time.time()
bubble_sort(numbers.copy())
bubble_time = time.time() - start_time

# Measure time for selection sort
start_time = time.time()
selection_sort(numbers.copy())
selection_time = time.time() - start_time

# Measure time for insertion sort
start_time = time.time()
insertion_sort(numbers.copy())
insertion_time = time.time() - start_time

# Plotting the results
labels = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
times = [bubble_time, selection_time, insertion_time]

plt.bar(labels, times, color=['red', 'green', 'blue'])
plt.xlabel('Sorting Algorithms')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.show()
