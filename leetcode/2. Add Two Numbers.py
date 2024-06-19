# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            column_sum = l1_value + l2_value + carry
            carry = column_sum // 10
            new_node = ListNode(column_sum % 10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next


node_1 = ListNode(2)
node_1.next = ListNode(4)
node_1.next.next = ListNode(3)

node_2 = ListNode(5)
node_2.next = ListNode(6)
node_2.next.next = ListNode(4)

solution = Solution()
s = solution.add_two_numbers(node_1, node_2)
print([s.val, s.next.val, s.next.next.val])
