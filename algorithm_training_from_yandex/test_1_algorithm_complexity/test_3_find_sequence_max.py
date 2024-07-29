import pytest


def find_sequence_max(seq):
    if len(seq) == 0:
        return '-inf'
    else:
        seqmax = seq[0]
        for i in range(1, len(seq)):
            if seq[i] > seqmax:
                seqmax = seq[i]
    return seqmax


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 3, 2], 3),
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
        ([1, 1, 1], 1),
        ([1], 1),
        ([], '-inf'),
        ([-2, -1, -3], -1),
    ],
)
def test_example(input, expected):
    assert find_sequence_max(input) == expected
