# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        dummy_node = ListNode(0, next=head)
        themap = {}
        cum_sum = 0
        current = dummy_node

        while current:
            cum_sum += current.val
            themap[cum_sum] = current
            current = current.next

        cum_sum = 0
        current = dummy_node

        while current:
            cum_sum += current.val
            current.next = themap[cum_sum].next
            current = current.next

        return dummy_node.next
