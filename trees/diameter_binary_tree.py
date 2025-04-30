# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        larg_dia=[0]
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            diameter=left+right
            larg_dia[0]=max(larg_dia[0],diameter)
            return 1+max(left,right)
        height(root)
        return larg_dia[0]


# do it as the calculation of height of the tree
   # time complexity O(N)
   # space complexity O(h) # call stack space complexity