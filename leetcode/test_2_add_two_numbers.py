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


class Tests:
    @staticmethod
    def __create_list_node(values_list):
        init_head = ListNode()
        curr = init_head
        for i in values_list:
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node
        return init_head.next

    @staticmethod
    def __print_all_links(linked_list):
        list_for_print = []
        end_of_linked_list = False
        while not end_of_linked_list:
            try:
                list_for_print.append(linked_list.val)
                linked_list = linked_list.next
            except AttributeError:
                end_of_linked_list = True
        return list_for_print

    def test_example_1(self):
        node_1 = self.__create_list_node([2, 4, 3])
        node_2 = self.__create_list_node([5, 6, 4])
        solution = Solution()
        s = solution.add_two_numbers(node_1, node_2)
        assert self.__print_all_links(s) == [7, 0, 8]

    def test_example_2(self):
        node_1 = self.__create_list_node([0])
        node_2 = self.__create_list_node([0])
        solution = Solution()
        s = solution.add_two_numbers(node_1, node_2)
        assert self.__print_all_links(s) == [0]

    def test_example_3(self):
        node_1 = self.__create_list_node([9, 9, 9, 9, 9, 9, 9])
        node_2 = self.__create_list_node([9, 9, 9, 9])
        solution = Solution()
        s = solution.add_two_numbers(node_1, node_2)
        assert self.__print_all_links(s) == [8, 9, 9, 9, 0, 0, 0, 1]
