def find_pair(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Test cases
nums1 = [8,7,2,5,3,1]
target1 = 10
print(find_pair(nums1, target1))  # Output: True

nums2 = [5,2,6,8,1,9]
target2 = 12
print(find_pair(nums2, target2))  # Output: False
