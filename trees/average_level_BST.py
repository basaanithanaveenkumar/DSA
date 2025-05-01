# Definition for a binary tree node.
#from __future__ import division 
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        q=deque()
        q.append(root)
        ans=[]

        while q:
            #node=q.popleft(#
            #val=[node.value]
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #print(l)
            sum_av=sum(l)
            print(sum_av)
            av= sum_av/len(l)

            ans.append(av)
        return ans