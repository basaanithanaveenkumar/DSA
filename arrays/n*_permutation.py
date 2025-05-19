# permutation from deep seek O(n!)

def permute_recursive(nums):


    # Base case: if list has only one element, return it as single permutation
    if len(nums) == 1:
        return [nums]
    
    result = []
    
    # Iterate through each element in the list
    for i in range(len(nums)):
        # Select current element as the first element
        current = nums[i]
        
        # Get all remaining elements except current
        remaining = nums[:i] + nums[i+1:]
        
        # Recursively generate permutations of remaining elements
        for p in permute_recursive(remaining):
            # Combine current element with each permutation of remaining elements
            result.append([current] + p)
    
    return result

"""Explination 



    if len(nums) == 1: return [nums]: Base case - single element has only one permutation

    result = []: Initialize empty list to store permutations

    for i in range(len(nums)):: Loop through each element index

    current = nums[i]: Select current element to be first in permutation

    remaining = nums[:i] + nums[i+1:]: Create list of all elements except current

    for p in permute_recursive(remaining):: Recursively get permutations of remaining elements

    result.append([current] + p): Combine current element with each sub-permutation

    return result: Return all permutations
    
    """