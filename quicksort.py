def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
if __name__ == "__main__":
    input_array = list(map(int, input("Enter the array elements separated by space: ").split()))
    sorted_array = quick_sort(input_array)
    print("Sorted array:", sorted_array)
