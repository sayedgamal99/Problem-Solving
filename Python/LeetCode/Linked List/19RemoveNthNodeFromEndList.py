# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head.next is None:
            return None
        dummy_node = ListNode(val=0, next=head)
        left = dummy_node
        right = head

        while n > 0 and right:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy_node.next
