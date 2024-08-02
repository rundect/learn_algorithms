import pytest


def best_team_sum(players):
    best_sum = 0
    now_sum = 0
    last = 0
    len_players = len(players)
    for first in range(len_players):
        while last < len_players and (last == first or players[first] + players[first + 1] >= players[last]):
            now_sum += players[last]
            last += 1
        best_sum = max(best_sum, now_sum)
        now_sum -= players[first]
    return best_sum


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 1, 3], 4),
        ([1, 1, 3, 3, 4, 6], 16),
        ([1, 1, 3, 3, 4, 6, 11], 17),
    ],
)
def test_example(input, expected):
    assert best_team_sum(input) == expected
