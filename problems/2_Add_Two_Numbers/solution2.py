"""
2. Add Two Numbers
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(-1)
        res_tail = res_head
        carry = 0

        while l1 or l2 or carry:
            if l1 and l2:
                temp = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                temp = l1.val + carry
                l1 = l1.next
            elif l2:
                temp = l2.val + carry
                l2 = l2.next
            elif carry:
                temp = carry

            carry = temp // 10
            res_tail.next = ListNode(temp % 10)
            res_tail = res_tail.next

        res_tail = None

        return res_head.next
