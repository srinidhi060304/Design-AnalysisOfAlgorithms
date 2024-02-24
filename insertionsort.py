def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Take input from the user
n = int(input("Enter the number of elements: "))
arr = []
for _ in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

print("Original array:", arr)

# Call the insertion sort function
insertion_sort(arr)

print("Sorted array:", arr)
