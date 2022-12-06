from puzzles.day_01 import part_1, part_2
from puzzles.utilities.dataframes import load
from puzzles.utilities.defs import TEST_INPUT_DATA

test_data = f"{TEST_INPUT_DATA}/day_01.txt"
test_df_1 = load(filename=test_data)
test_df_2 = load(filename=test_data)


def test_part_1():

    result = part_1(df=test_df_1)

    assert result == 24000


def test_part_2():

    result = part_2(df=test_df_2)

    assert result == 45000
