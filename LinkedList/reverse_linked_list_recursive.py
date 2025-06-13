# recursive linked list is tricky please follow the below link : https://takeuforward.org/data-structure/reverse-a-linked-list/


def reverseList(head):
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    reversed_head = reverseList(head.next)
    
    # Make the next node point back to current node
    head.next.next = head
    
    # Break the original link
    head.next = None
    
    return reversed_head

"""

Step-by-Step Execution

Let's visualize reversing 1 → 2 → 3 → 4 → None

    Initial call: reverseList(1)

        Recurses to reverseList(2)

            Recurses to reverseList(3)

                Recurses to reverseList(4)

                    Base case reached (4.next is None), returns 4

                Now head is 3

                3.next.next = 3 (makes 4 point to 3)

                3.next = None

                Returns 4 → 3 → None

            Now head is 2

            2.next.next = 2 (makes 3 point to 2)

            2.next = None

            Returns 4 → 3 → 2 → None

        Now head is 1

        1.next.next = 1 (makes 2 point to 1)

        1.next = None

        Returns 4 → 3 → 2 → 1 → None"""