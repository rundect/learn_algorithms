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


def create_list_node(values_list):
    init_head = ListNode()
    curr = init_head
    for i in values_list:
        new_node = ListNode(i)
        curr.next = new_node
        curr = new_node
    return init_head.next


def print_all_links(linked_list):
    list_for_print = []
    end_of_linked_list = False
    while not end_of_linked_list:
        list_for_print.append(linked_list.val)
        linked_list = linked_list.next


# node_1 = ListNode(2)
# node_1.next = ListNode(4)
# node_1.next.next = ListNode(3)
#
# node_2 = ListNode(5)
# node_2.next = ListNode(6)
# node_2.next.next = ListNode(4)
# print([s.val, s.next.val, s.next.next.val])

def test_one():
    node_1 = create_list_node([9, 9, 9, 9, 9, 9, 9])
    node_2 = create_list_node([9, 9, 9, 9])
    solution = Solution()
    s = solution.add_two_numbers(node_1, node_2)
    assert print_all_links(s) == [8, 9, 9, 9, 0, 0, 0, 1]
