"""
19. Remove Nth Node From End of List
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Beats 100.00% | Beats 84.64%
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        read_ptr = head

        for _ in range(n):
            read_ptr = read_ptr.next

        n_ptr = head
        n_prev_ptr = None

        while read_ptr is not None:
            read_ptr = read_ptr.next

            n_prev_ptr = n_ptr
            n_ptr = n_ptr.next

        if n_ptr == head:
            head = head.next
        else:
            n_prev_ptr.next = n_ptr.next

        return head


# 0     1    2   3    4
# [] > [] > [] > [] > []


# 3 cases:
# 1. len = n
# 2. 0 < n < len
# 3. n = 0
