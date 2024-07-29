import pytest


def find_most_common_char(s):
    ans = ''
    anscnt = 0
    dct = {}
    for now in s:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for key in dct:
        if dct[key] > anscnt:
            anscnt = dct[key]
            ans = key
    return ans


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ('ababa', 'a'),
    ],
)
def test_example(input, expected):
    assert find_most_common_char(input) == expected
