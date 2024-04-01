import random
import time
import matplotlib.pyplot as plt

# Generate random array of size 10000 with elements in range 1 to 1000
arr = [random.randint(1, 1000) for _ in range(10000)]

# Linear search algorithm
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary search algorithm
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to measure the execution time of a given function
def measure_execution_time(func, arr, key):
    start_time = time.time()
    result = func(arr, key)
    end_time = time.time()
    return end_time - start_time

# Main function to perform searches and plot execution times
def main():
    search_key = int(input("Enter the search key: "))
    linear_times = []
    binary_times = []

    for _ in range(5):
        linear_time = measure_execution_time(linear_search, arr, search_key)
        binary_time = measure_execution_time(binary_search, sorted(arr), search_key)
        linear_times.append(linear_time)
        binary_times.append(binary_time)

    # Plotting the results
    plt.plot(range(1, 6), linear_times, label='Linear Search')
    plt.plot(range(1, 6), binary_times, label='Binary Search')
    plt.xlabel('Search Attempt')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time of Linear vs Binary Search')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
