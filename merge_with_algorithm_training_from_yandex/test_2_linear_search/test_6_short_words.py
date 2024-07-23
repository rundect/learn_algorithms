import pytest


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


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (['aa', 'b', 'cc', 'd'], 'b d'),
        (['a', 'b', 'c'], 'a b c'),
        (['a', ''], ''),
    ],
)
def test_example(input, expected):
    assert short_words(input) == expected
