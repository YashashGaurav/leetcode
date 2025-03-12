"""
21. Merge Two Sorted Lists
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        combined_list_head: ListNode = ListNode(-200, None)
        combined_list_tail: ListNode = combined_list_head

        while list1 is not None or list2 is not None:
            if list1 is None and list2 is None:
                break

            if list1 is None:
                combined_list_tail.next = list2
                list2 = list2.next
                combined_list_tail = combined_list_tail.next
                break

            if list2 is None:
                combined_list_tail.next = list1
                list1 = list1.next
                combined_list_tail = combined_list_tail.next
                break

            if list1.val <= list2.val:
                combined_list_tail.next = list1
                list1 = list1.next
                combined_list_tail = combined_list_tail.next
            else:
                combined_list_tail.next = list2
                list2 = list2.next
                combined_list_tail = combined_list_tail.next

        return combined_list_head.next


# list1 = [1,2,4], list2 = [1,3,4]
# list1 = [val = 1, next = [val = 2]]
# list2 = [val = 1, next = [val = 3]]
# combined_list_head = None
# combined_list_tail = None
