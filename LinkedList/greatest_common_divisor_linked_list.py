# Definition for singly-linked list.
import math
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=head
        curr=head.next
        while curr:
            g=math.gcd(prev.val,curr.val)
            prev.next=ListNode(g)
            g.next=curr
            prev=curr
            curr=curr.next
        return head

        