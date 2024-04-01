# a. 𝑂(𝑛^2) algorithm
def has_pair_sum_n2(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

# b. 𝑂(𝑛𝑙𝑜𝑔𝑛) algorithm
def has_pair_sum_nlogn(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

# Test case
arr = [8, 4, 1, 6]
K = 10
print(has_pair_sum_n2(arr, K))  # Output: True (4 + 6 = 10)
print(has_pair_sum_nlogn(arr, K))  # Output: True (4 + 6 = 10)
