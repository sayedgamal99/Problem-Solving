# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        node = head
        prevnode = None
        while node:
            nextnode = node.next
            node.next = prevnode
            prevnode = node
            node = nextnode

        return prevnode
