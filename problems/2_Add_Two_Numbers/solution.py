from typing import Union


class ListNode:
    def __init__(self, val: int = 0, next: Union["ListNode", None] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_list: Union[ListNode, None] = None
        head: Union[ListNode, None] = None
        carry: int = 0
        while True:
            new_return_node = ListNode(
                int((l1.val + l2.val + carry) % 10), None
            )
            carry = int((l1.val + l2.val + carry) / 10)
            if return_list is None:
                return_list = head = new_return_node
            else:
                head.next = new_return_node
                head = head.next

            if (l1.next is not None) and (l2.next is not None):
                l1 = l1.next
                l2 = l2.next
            elif l1.next is not None and l2.next is None:
                l1 = l1.next
                l2 = ListNode()
            elif l1.next is None and l2.next is not None:
                l1 = ListNode()
                l2 = l2.next
            else:
                if carry != 0:
                    l1 = ListNode(carry, None)
                    l2 = ListNode()
                    carry = 0
                else:
                    break

        return return_list


solution = Solution()
output = solution.addTwoNumbers(
    ListNode(
        9,
        ListNode(
            9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
        ),
    ),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
)
print(output)
