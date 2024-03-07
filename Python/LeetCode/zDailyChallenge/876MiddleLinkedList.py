# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        node = head
        size = 0
        while node:
            size += 1
            node = node.next

        node = head
        cur = 0
        while node:
            if cur == (size//2):
                return node
            cur += 1
            node = node.next
