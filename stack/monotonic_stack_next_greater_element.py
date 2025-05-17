def nextGreaterElement(nums):
    stack = []          # Maintains a decreasing order of elements
    res = [-1] * len(nums)  # Result array initialized to -1

    # Iterate from the end of the array to the start
    for i in range(len(nums)-1, -1, -1):
        # Pop elements <= current element (they can't be the next greater)
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # Update result if stack has elements left
        res[i] = stack[-1] if stack else -1

        # Push current element to the stack
        stack.append(nums[i])
    
    return res


def previous_greater_elements(nums):
    res = []
    stack = []

    for num in nums:
        while stack and stack[-1] <= num:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(num)

    return res
