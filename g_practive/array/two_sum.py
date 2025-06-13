# patterns to solve the two sum
"""1. using the hash-map
2. using two pointers"""

def two_sum_two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]  # or return [nums[left], nums[right]] if you want the values
        elif current_sum < target:
            left += 1  # we need a larger sum, move left pointer right
        else:
            right -= 1  # we need a smaller sum, move right pointer left
    
    return []  # no solution found



def two_sum_hash_map(nums, target):
    num_map = {}  # value to index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return [] 