# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]


        """
        dummy=ListNode()
        dummy.next=head
        beh=ahead=dummy
        for _ in range(n+1):
            ahead=ahead.next
        while ahead:
            beh=beh.next
            ahead=ahead.next
        beh.next=beh.next.next
        return dummy.next
        # its the reverse way of dealing with problem 