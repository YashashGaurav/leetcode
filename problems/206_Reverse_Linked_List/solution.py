"""
    206. Reverse Linked List
"""

from typing import Optional, List

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


# Accepted	82 ms	15.5 MB
class Solution0:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return

        root = head
        head_next = head.next

        while head_next != None:
            # save states
            head_next_next = head_next.next
            # move pointers
            head_next.next = head
            head = head_next
            head_next = head_next_next
            continue
        else:
            root.next = None
            return head


# Accepted	44 ms	15.4 MB
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        while head != None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            continue

        return prev


# Accepted	33 ms	20.3 MB
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)

    def _reverse(self, head, prev=None):
        if head == None:
            return prev

        next = head.next
        head.next = prev
        prev = head
        head = next
        return self._reverse(head, prev)


ll = LinkedList()
ll.create_list([1, 2, 3, 4, 5])
print(ll.print_ll(Solution().reverseList(ll.root)))

ll = LinkedList()
ll.create_list([1, 2])
print(ll.print_ll(Solution().reverseList(ll.root)))

ll = LinkedList()
ll.create_list([])
print(ll.print_ll(Solution().reverseList(ll.root)))
