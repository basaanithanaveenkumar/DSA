# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same_tree(p,q):
            if not p and not q:
                return True
            if p and not q or q and not p:
                return False
            if p.val!=q.val:
                return False
            return same_tree(p.left,q.left) and same_tree(p.right,q.right)
        def same_sub_tree(root):
            if not root:
                return False
            if  same_tree(root,subRoot):
                return True
            return same_sub_tree(root.left) or same_sub_tree(root.right)
        return same_sub_tree(root)
        # Need to find the iterative way of solving it
        # Time complity o(m*n) --> suboptimal not good
        # space o(n)