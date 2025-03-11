"""
141. Linked List Cycle
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Floyd's Tortoise and Hare
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tortoise, hare = head, head

        while tortoise:
            tortoise = tortoise.next
            if tortoise is None:
                return False
            hare = hare.next.next
            if hare is None or hare.next is None:
                return False

            if hare is tortoise:
                return True

    # visitedSet Solution
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        if not head:
            return False

        while head:
            if head in visited:
                return False
            visited.add(head)
            head = head.next

        return True
