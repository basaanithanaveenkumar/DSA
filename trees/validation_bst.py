# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node.left:
                if node.val<node.left.val:
                    return False
            if node.right:
                if  node.val>node.right.val:
                    return False
            if node.right:
                q.append(node.left)
            if node.left:
                q.append(node.right)
        return True 
# self completion