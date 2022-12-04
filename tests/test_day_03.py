from day03 import create_df, part_1, part_2
from utilities.dataframes import load

test_data = "./data/day_03.txt"
test_df_1 = load(filename=test_data)
test_df_2 = load(filename=test_data)


def test_sum_priorities():
    result = part_1(df=test_df_1)

    assert result == 157


def test_groups():
    result = part_2(df=test_df_2)

    assert result == 70
