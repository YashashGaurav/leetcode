"""
143. Reorder List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 29.39% | 38.92%
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the list:
        fast, slow = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        curr_2 = mid.next
        prev_2 = None
        mid.next = None

        # reverse till mid:
        while curr_2 is not None:
            curr_2_next = curr_2.next
            curr_2.next = prev_2

            prev_2 = curr_2
            curr_2 = curr_2_next

        reverse_head = prev_2

        # merge:
        curr = head
        while reverse_head is not None:
            curr_next = curr.next
            reverse_head_next = reverse_head.next

            curr.next = reverse_head
            reverse_head.next = curr_next
            curr = curr_next
            reverse_head = reverse_head_next

        return head
