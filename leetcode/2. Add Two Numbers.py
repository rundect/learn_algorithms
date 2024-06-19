# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        init_head = ListNode()
        current_node = init_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            sum_value = value_1 + value_2 + carry
            carry = sum_value // 10
            node = ListNode(sum_value % 10)
            current_node.next = node
            current_node = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return init_head.next


node_1 = ListNode(2)
node_1.next = ListNode(4)
node_1.next.next = ListNode(3)

node_2 = ListNode(5)
node_2.next = ListNode(6)
node_2.next.next = ListNode(4)

solution = Solution()
s = solution.add_two_numbers(node_1, node_2)
print([s.val, s.next.val, s.next.next.val])


node_1 = ListNode(9)
node_1.next = ListNode(9)
node_1.next.next = ListNode(9)
node_1.next.next.next = ListNode(9)
node_1.next.next.next.next = ListNode(9)
node_1.next.next.next.next.next = ListNode(9)
node_1.next.next.next.next.next.next = ListNode(9)

node_2 = ListNode(9)
node_2.next = ListNode(9)
node_2.next.next = ListNode(9)
node_2.next.next.next = ListNode(9)

solution = Solution()
s = solution.add_two_numbers(node_1, node_2)
print(
    [
        s.val,
        s.next.val,
        s.next.next.val,
        s.next.next.next.val,
        s.next.next.next.next.val,
        s.next.next.next.next.next.val,
        s.next.next.next.next.next.next.val,
        s.next.next.next.next.next.next.next.val,
    ]
)
