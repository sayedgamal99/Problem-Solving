# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# using set solution:

class Solution:
    def hasCycle(self, head) -> bool:
        theset = set()
        node = head
        while node:
            if node in theset:
                return True
            else:
                theset.add(node)
            node = node.next
        return False

# another solution without extra memory: using two pointer ( one fast and one slow)
# ACCEPTED


class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        l = head
        r = head.next
        while r and r.next:
            if l == r:
                return True
            l = l.next
            r = r.next
            if l and r and l == r:
                return True
            r = r.next
        return False
