import heapq

def find_k_largest(arr, k):
    return heapq.nlargest(k, arr)

# Example array
arr = [3, 10, 4, 7, 15, 20, 1, 9]
k = 3

result = find_k_largest(arr, k)
print(result)
