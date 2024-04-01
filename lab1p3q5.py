def merge(arr, left, mid, right):
    inv_count = 0
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inv_count += (n1 - i)
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return inv_count

def merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, left, mid)
        inv_count += merge_sort(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)

    return inv_count

def inversion_count(arr):
    return merge_sort(arr, 0, len(arr) - 1)

# Test case
A = [10, 1, 2, 4, 13, 9, 5]
print("The number of inversions:", inversion_count(A))  # Output: 8
