from puzzles.day_06 import part_1, part_2
from puzzles.utilities.dataframes import load
from puzzles.utilities.defs import TEST_INPUT_DATA

test_data = f"{TEST_INPUT_DATA}/day_06.txt"


def test_part_1():
    result = part_1(filename=test_data, marker_len=4)

    assert result == 7


def test_part_2():
    result = part_1(filename=test_data, marker_len=14)

    assert result == 19
