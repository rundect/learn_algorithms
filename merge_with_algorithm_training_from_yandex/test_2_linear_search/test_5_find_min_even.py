
def find_min_even(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans


class Tests:
    def test_example_1(self):
        seq = [2, 4, 6]
        s = find_min_even(seq)
        assert s == 2

    def test_example_2(self):
        seq = [3, 1]
        s = find_min_even(seq)
        assert s == -1

    def test_example_3(self):
        seq = [-1, -2]
        s = find_min_even(seq)
        assert s == -2

    def test_example_4(self):
        seq = [0, 2]
        s = find_min_even(seq)
        assert s == 0

    def test_example_5(self):
        seq = []
        s = find_min_even(seq)
        assert s == -1
