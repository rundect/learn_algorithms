
def short_words(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


class Tests:
    def test_example_1(self):
        words = ['aa', 'b', 'cc', 'd']
        s = short_words(words)
        assert s == 'b d'

    def test_example_2(self):
        words = ['a', 'b', 'c']
        s = short_words(words)
        assert s == 'a b c'

    def test_example_3(self):
        words = ['a', '']
        s = short_words(words)
        assert s == ''
