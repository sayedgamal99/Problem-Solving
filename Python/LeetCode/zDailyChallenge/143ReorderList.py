# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        newlist, size = self.copyList(head)
        reversed_new_list = self.reverseList(newlist)
        Node = head
        revNode = reversed_new_list
        s = 1
        while True:
            if s+1 <= size:
                nextNode = Node.next
                Node.next = revNode
                s += 1
            else:
                Node.next = None
                break
            Node = nextNode
            if s+1 <= size:
                nextNode = revNode.next
                revNode.next = Node
                s += 1
            else:
                revNode.next = None
                break
            revNode = nextNode

    # create linked list copy:

    def copyList(self, head):
        newHead = ListNode(head.val)
        new, node = newHead, head
        size = 1
        while node.next:
            new.next = ListNode(node.next.val)
            new = new.next
            node = node.next
            size += 1
        return newHead, size

    # reverse copy:

    def reverseList(self, head):
        node = head
        prevnode = None
        while node:
            nextnode = node.next
            node.next = prevnode
            prevnode = node
            node = nextnode
        return prevnode
