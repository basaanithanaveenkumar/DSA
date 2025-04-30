# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def same(p,q):
            # base case
            if not p and not q:
                return False
            if (p and not q) and (q and not p):
                return False
            if p.val!=q.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)
        return same(p,q)
        
        # not working yest
        # time complexity (o(m+n)) # as its a 2 trees