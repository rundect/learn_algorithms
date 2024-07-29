import pytest


def find_sequence_sum(seq):
    seqsum = 0
    for i in range(len(seq)):
        seqsum += seq[i]
    return seqsum


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([4, 1, 0, 6], 11),
    ],
)
def test_example(input, expected):
    assert find_sequence_sum(input) == expected
