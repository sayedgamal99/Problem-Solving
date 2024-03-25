# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        node1, node2 = list1, list2
        if not node1:
            return node2
        elif not node2:
            return node1
        elif not (node1 and node2):
            return None

        newList = ListNode(None, None)
        new = newList
        while node1 and node2:
            if node1.val <= node2.val:
                new.next = ListNode(node1.val)
                node1 = node1.next
            else:
                new.next = ListNode(node2.val)
                node2 = node2.next
            new = new.next

        if node1:
            new.next = node1
        elif node2:
            new.next = node2

        return newList.next


# ----------------------------- running the code ------------------------
# Create two linked lists
# List 1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# List 2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Instantiate the Solution class
solution = Solution()

# Merge the two lists
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list values
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else '')
    merged_list = merged_list.next
