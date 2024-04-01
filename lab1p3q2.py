def max_product_pair(nums):
    if len(nums) < 2:
        return None
    
    nums.sort()
    return nums[-1] * nums[-2]

# Test case
nums = [1, 7, 4, 2, 8, 6, 3, 9, 5]
print(max_product_pair(nums))  # Output: 72
