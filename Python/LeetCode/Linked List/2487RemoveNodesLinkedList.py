# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        stack = []
        node = head
        while node:
            while stack and node.val > stack[-1]:
                stack.pop()
            stack.append(node.val)

            node = node.next
        head = ListNode(stack[0], None)
        node = head
        i = 1
        while i < len(stack):
            node.next.val = ListNode(stack[i], None)
            i += 1
        return head
