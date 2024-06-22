class BinarySearch:
    def __init__(self, list, item, low=0, high=0):
        self.list = list
        self.item = item
        self.low = low
        self.high = high

    def search_iterative(self):
        low = 0
        high = len(self.list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = self.list[mid]
            if guess == self.item:
                return mid
            if guess > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def search_recursive(self):
        if self.high >= self.low:
            mid = (self.high + self.low) // 2
            guess = self.list[mid]
            if guess == self.item:
                return mid
            elif guess > self.item:
                bs = BinarySearch(self.list, self.item, self.low, mid - 1)
                return bs.search_recursive()
            else:
                bs = BinarySearch(self.list, self.item, mid + 1, self.high)
                return bs.search_recursive()
        else:
            return None
