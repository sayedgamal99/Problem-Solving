# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        middle = self.middle(head)
        reversedM = self.reverse(middle)
        return self.Palindrom(head, reversedM)

    def middle(self, head):
        # find the middle to compare second part with first
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, new_head):
        # reverse copied list
        node = new_head
        prevnode = None
        while node:
            nextnode = node.next
            node.next = prevnode
            prevnode = node
            node = nextnode
        return prevnode

    def Palindrom(self, head, prevnode):
        # traverse the copy and check for palindrom
        nodeCopy = prevnode
        nodeOriginal = head
        while nodeCopy and nodeOriginal:
            if nodeCopy.val != nodeOriginal.val:
                return False
            nodeOriginal = nodeOriginal.next
            nodeCopy = nodeCopy.next
        return True
