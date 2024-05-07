# Definition for singly-linked list.

import sys
sys.set_int_max_str_digits(0)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        number = []
        node = head
        while node:
            number.append(f'{node.val}')
            node = node.next

        number = list(str(int(''.join(number))*2))

        newHead = ListNode(number[0])
        node = newHead
        for i in number[1:]:
            node.next = ListNode(i)
            node = node.next
        return newHead
