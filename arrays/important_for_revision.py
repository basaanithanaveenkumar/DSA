Interview revision:
sliding window: https://www.youtube.com/watch?v=GaXwHThEgGk&t=438s&ab_channel=GregHogg

1. work@tech most asked questions -- based on accuracy
2. Greg hog @ most asked questions company wise
3. neetcode @ most asked question company wise
4.faraz most asked question company wise
5. Leet code most asked question comapny wise

pattersn: 
1. sort and look for solution
2. look from last and look for solution
3. Loot at both the ends and look for solution 


1. Bitmanipulation

sol[:] --> solution copy

# concepts that are hard to grasp and unexplored
-- Recursive backtracking
-- Tries

# Notes from anusharma youtube
 Array / String Inputs

1. Is the array sorted?
→ Use Binary Search, Two Pointers, or Prefix Sums

2. Optimization problems (Max/Min/Subarray)?
→ Think Sliding Window, Dynamic Programming, or Greedy

3. Looking for duplicates / counts / frequencies?
→ Use HashMap, HashSet, or Counting Array

4. Need substrings or fixed-size subarrays?
→ Apply Sliding Window with Two Pointers

5. Frequent min/max in window?
→ Use Monotonic Queue, Deque, or Heap

6. Generating subsets, permutations, combinations?
→ Use Backtracking

7. Matching / parsing characters?
→ Use Stack, especially for Balanced Parentheses, Infix/Postfix







Maximum sub array--> https://www.youtube.com/shorts/lrH2sw-FmD4


# find the difference between subarray and sub sequence


Merge sort: https://www.youtube.com/shorts/7PcqoMWbxN8

# write the code for merge sort in an explainable way

https://www.linkedin.com/posts/harsadash_leetcode-activity-7331896595640197120-L4cg?utm_source=share&utm_medium=member_desktop&rcm=ACoAACQXQ4QBqLfzuvb2q_NwRd8JuUkBVTumfIk

https://www.youtube.com/shorts/QBoXIg4ucos

# get the reverse indexes
for i in reversed(range(5)):  # 4, 3, 2, 1, 0 (descending)
    print(i)

# belmen floyds algorithm
https://www.youtube.com/watch?v=5eIK3zUdYmE&ab_channel=NeetCode


stack using the singly linked list

Yes, we can definitely implement a stack using a singly linked list. The key idea is to maintain the top of the stack as the head of the linked list, allowing all operations (push, pop, peek) to be performed in O(1) time.

stack and queue basics: https://youtu.be/vOx3vY1w4tM?si=o20GhxTQnLvDHCjG


Monotonic stack: https://www.youtube.com/watch?v=e7XQLtOQM3I&ab_channel=takeUforward

LRU cache: very important topic --> https://www.youtube.com/watch?v=z9bJUPxzFOw&ab_channel=takeUforward


find if a bit is set or not (n&(1<<i))!=0 # for the bit manipulation

power set using bit mainpulation : https://www.youtube.com/watch?v=b7AYbpM5YrE&ab_channel=takeUforward

def power_set(nums):
    n = len(nums)
    power_set_size = 1 << n  # 2^n
    power_set = []

    for i in range(power_set_size):
        subset = []
        for j in range(n):
            # Check if j-th bit is set in i
            if (i >> j) & 1:
                subset.append(nums[j])
        power_set.append(subset)
    
    return power_set

# Example Usage
nums = [1, 2, 3]
print(power_set(nums))


combination sum : --> recursive backtracking : https://youtube.com/shorts/qV20jACVNS4?si=sKi9nI6JnFXyTVwf
combination sum full video : https://www.youtube.com/watch?v=GBKI9VSKdGg&ab_channel=NeetCode




python questions
what is decorator
what is iterator in python



# first find the how DFS works in recursion
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build a simple tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def dfs_tree(node):
    if not node:
        return
    print(node.val, end=" ")  # Process the node (Pre-Order)
    dfs_tree(node.left)        # Traverse left
    dfs_tree(node.right)       # Traverse right

print("\nDFS on Binary Tree (Pre-Order):")
dfs_tree(root)

#  write  the code for pre order and post order traversal, 
#  write the code for inorder traversal code 
# 
# leval order traversal (BFS)

# find the height of atree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

# Example Usage:
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')

print("Height of the tree:", height(root))  # Output: 3



def diameterOfBinaryTree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left + right)  # Update diameter
        return 1 + max(left, right)  # Return height

    height(root)
    return diameter

# Same example as before:
print("Optimized Diameter:", diameterOfBinaryTree(root))  # Output: 4



CUDA;
https://www.linkedin.com/posts/sanket-shah-33a3a2135_nvidia-cuda-hpc-activity-7334672304687243264-Xd--?utm_source=share&utm_medium=member_desktop&rcm=ACoAACQXQ4QBqLfzuvb2q_NwRd8JuUkBVTumfIk




# preparation
1. Graphs 

   multi source BFS
   digistra algorithm
   bellman fords algorithm

2. Trees 
3. Dynamic programming
4. Recursive backtracking
5. sliding window

1. solve the patterns in each topic
1. Dynamic programming: 




1.SOlve Most asked company questions