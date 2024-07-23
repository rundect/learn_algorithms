import pytest


def rle(s):
    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)


def pack(s, cnt):
    if cnt > 1:
        return s + str(cnt)
    return s


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB', 'A4B3C2XYZD4E3F3A6B28'),
        ('aabbca', 'a2b2ca'),
    ],
)
def test_example(input, expected):
    assert rle(input) == expected
