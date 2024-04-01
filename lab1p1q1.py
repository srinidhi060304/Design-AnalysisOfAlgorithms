import time
import matplotlib.pyplot as plt
import sys

# Set recursion limit to prevent exceeding maximum recursion depth
sys.setrecursionlimit(10**6)

# Iterative algorithm to calculate the sum of first N natural numbers
def iterative_sum(N):
    result = 0
    for i in range(1, N + 1):
        result += i
    return result

# Recursive algorithm to calculate the sum of first N natural numbers
def recursive_sum_helper(N, current_sum):
    if N == 0:
        return current_sum
    else:
        return recursive_sum_helper(N - 1, current_sum + N)

def recursive_sum(N):
    return recursive_sum_helper(N, 0)

# Function to measure the execution time of a given function for a given input
def measure_execution_time(func, N):
    start_time = time.time()
    result = func(N)
    end_time = time.time()
    return end_time - start_time

# Main function to plot the execution time of iterative and recursive algorithms
def plot_execution_time(max_N):
    iterative_times = []
    recursive_times = []
    N_values = list(range(1, max_N + 1))

    for N in N_values:
        iterative_time = measure_execution_time(iterative_sum, N)
        recursive_time = measure_execution_time(recursive_sum, N)
        iterative_times.append(iterative_time)
        recursive_times.append(recursive_time)

    plt.plot(N_values, iterative_times, label='Iterative')
    plt.plot(N_values, recursive_times, label='Recursive')
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time of Iterative vs Recursive Sum Calculation')
    plt.legend()
    plt.show()

# Define the maximum value of N for plotting
max_N = 1000
plot_execution_time(max_N)
