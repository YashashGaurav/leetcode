"""
206. Reverse Linked List
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# defining LinkedList for debugging
class LinkedList:
    def __init__(self):
        self.root: ListNode = None
        self.head: ListNode = None

    def add_node(self, node: ListNode):
        if self.root == None:
            self.root = node
            self.head = self.root

        self.head.next = node
        self.head = node

    def create_list(self, arr: List):
        for i in arr:
            self.add_node(ListNode(i))

    @classmethod
    def print_ll(cls, head: ListNode):
        current: ListNode = head
        while current != None:
            print(current.val)
            current = current.next
            continue


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse_list(head, prev=None):
            if head is None:
                return prev

            curr = head
            head = head.next
            curr.next = prev

            return _reverse_list(head, curr)

        return _reverse_list(head)

    def reverseList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        head = head.next
        prev.next = None

        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev


ll = LinkedList()
ll.create_list([1, 2, 3, 4, 5])
print(ll.print_ll(Solution().reverseList(ll.root)))
