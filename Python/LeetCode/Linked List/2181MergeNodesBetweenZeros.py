class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        current = head.next  # Skip the initial 0 node
        merged_sum = 0
        merged_list_head = merged_list_tail = None

        while current:
            if current.val != 0:
                merged_sum += current.val
            else:
                # When a 0 is encountered, create a new node with the merged sum
                if merged_list_head is None:
                    merged_list_head = merged_list_tail = ListNode(merged_sum)
                else:
                    merged_list_tail.next = ListNode(merged_sum)
                    merged_list_tail = merged_list_tail.next
                merged_sum = 0  # Reset merged_sum after adding to the new list
            current = current.next

        return merged_list_head
