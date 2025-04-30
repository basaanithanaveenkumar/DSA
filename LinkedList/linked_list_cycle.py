# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d_node=ListNode()
        d_node.next=head
        slow=fast=d_node
        while fast and fast.next:
            fast= fast.next.next
            slow=slow.next
            if slow is fast:
                return True
        return False
        
        #Time-O(N)
        # space=0(1)

        # this can be ssolved using set as well