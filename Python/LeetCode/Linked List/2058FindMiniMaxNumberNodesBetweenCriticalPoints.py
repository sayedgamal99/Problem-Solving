class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_critical = last_critical = -1
        min_distance = float('inf')
        prev_critical_index = -1
        index = 1
        prev, curr = head, head.next

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if prev_critical_index != -1:
                    min_distance = min(
                        min_distance, index - prev_critical_index)
                prev_critical_index = index
                if first_critical == -1:
                    first_critical = index
                last_critical = index

            prev = curr
            curr = curr.next
            index += 1

        if first_critical == last_critical:
            return [-1, -1]

        return [min_distance, last_critical - first_critical]
