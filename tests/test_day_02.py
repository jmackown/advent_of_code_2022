from puzzles.day_02 import part_1, part_2
from puzzles.utilities.dataframes import load
from puzzles.utilities.defs import TEST_INPUT_DATA

test_data = f"{TEST_INPUT_DATA}/day_02.txt"
test_df_1 = load(filename=test_data)
test_df_2 = load(filename=test_data)


def test_get_total_score():

    expected_result = 15

    result = part_1(df=test_df_1)

    assert result == expected_result


def test_get_shapes():
    result = part_2(df=test_df_2)

    assert result == 12
