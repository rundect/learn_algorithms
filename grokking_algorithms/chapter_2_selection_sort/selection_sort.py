class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def __find_smallest(self):
        smallest = self.arr[0]
        smallest_index = 0
        for i in range(1, len(self.arr)):
            if self.arr[i] < smallest:
                smallest_index = i
                smallest = self.arr[i]
        return smallest_index

    def selection_sort(self):
        new_arr = []
        for i in range(len(self.arr)):
            smallest = self.__find_smallest()
            new_arr.append(self.arr.pop(smallest))
        return new_arr
