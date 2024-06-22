from selection_sort import SelectionSort


class TestSelectionSort:
    def test_selection_sort(self):
        arr = [5, 3, 6, 2, 10]
        sorting_class = SelectionSort(arr)
        sorted_array = sorting_class.selection_sort()
        assert sorted_array == [2, 3, 5, 6, 10]
