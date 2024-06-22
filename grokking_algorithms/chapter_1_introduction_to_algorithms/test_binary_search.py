from binary_search import BinarySearch
import json
import time

with open("items.json", "r") as file:
    data = json.load(file)

simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]


class TestBinarySearch:
    def test_iterative_binary_search(self):
        item, expected_index = 3, 1
        bs = BinarySearch([1, 3, 5, 7, 9], item)
        index = bs.search_iterative()
        assert index == expected_index

    def test_iterative_binary_search_none(self):
        item, expected_index = -1, None
        bs = BinarySearch([1, 3, 5, 7, 9], item)
        index = bs.search_iterative()
        assert index == expected_index

    def test_iterative_binary_search_with_simple_list(self):
        item, expected_index = 3, 1
        bs = BinarySearch(simple_list, item)
        index = bs.search_iterative()
        assert index == expected_index

    def test_recursive_binary_search_with_simple_list(self):
        item, expected_index = 3, 1
        low, high = 0, len(simple_list) - 1
        bs = BinarySearch(simple_list, item, low, high)
        index = bs.search_recursive()
        assert expected_index == index

    def test_search_for_nonexistent_item(self):
        item, expected_result = 100, None
        bs = BinarySearch(simple_list, item)
        index = bs.search_iterative()
        assert expected_result == index

    def test_binary_search_and_linear_search_execution_time(self):
        item, expected_index = 9887, 990
        start_time = time.time()
        bs = BinarySearch(list_with_1000_items, item)
        binary_search_index = bs.search_iterative()
        bs_time = time.time() - start_time
        start_time = time.time()
        linear_search_index = list_with_1000_items.index(item)
        ls_time = time.time() - start_time
        print(bs_time, ls_time)
        assert expected_index == binary_search_index
        assert expected_index == linear_search_index
        assert bs_time < ls_time

    def test_execution_time_for_item_at_the_beginning(self):
        item, expected_index = 55, 10
        start_time = time.time()
        bs = BinarySearch(list_with_1000_items, item)
        binary_search_index = bs.search_iterative()
        bs_time = time.time() - start_time

        start_time = time.time()
        linear_search_index = list_with_1000_items.index(item)
        ls_time = time.time() - start_time
        print(bs_time, ls_time)
        assert expected_index == binary_search_index
        assert expected_index == linear_search_index
        assert bs_time > ls_time
