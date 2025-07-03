"""
23. Merge k Sorted Lists
"""

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 77.78% (O(nlog(k))) | 17.88% O(nk)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorter = []

        # 1. Add a counter for tie-breaking
        counter = 0

        for list in lists:
            if not list:
                continue
            curr = list

            while curr:
                counter += 1
                heapq.heappush(sorter, (curr.val, counter, curr))
                curr = curr.next

        res_head = ListNode(-1)
        res_tail = res_head
        while sorter:
            _, _, node = heapq.heappop(sorter)
            res_tail.next = node
            res_tail = res_tail.next

        return res_head

    # 9.76% O(n.k) | 36.31% O(1)
    def mergeKLists_0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # clean_list
        clean_list = []
        for list_node in lists:
            if list_node:
                clean_list.append(list_node)
        lists = clean_list

        if not lists or len(lists) == 0:
            return None

        res_head = ListNode(-1)
        res_tail = res_head

        def find_list_min_index(lists):
            min_index, min_value = -1, 1e9

            for node_idx, node in enumerate(lists):
                if min_value > node.val:
                    min_value = node.val
                    min_index = node_idx

            return min_index

        while len(lists) > 0:
            min_idx = find_list_min_index(lists)

            temp = lists[min_idx]

            if lists[min_idx].next == None:
                lists = lists[:min_idx] + lists[min_idx + 1 :]
            else:
                lists[min_idx] = lists[min_idx].next

            res_tail.next = temp
            res_tail = res_tail.next

        return res_head.next
