def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Sort each bucket
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate sorted buckets
    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

# Take user input for the array
input_str = input("Enter space-separated numbers: ")
arr = list(map(float, input_str.split()))

# Apply bucket sort
bucket_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
