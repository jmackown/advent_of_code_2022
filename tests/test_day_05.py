from day_05 import part_1
from utilities.dataframes import load

test_data = "./data/day_05.txt"
# test_df_1 = load(filename=test_data)
# test_df_2 = load(filename=test_data)


def test_part_1():
    result = part_1(filename=test_data)

    assert result == "CMZ"


# def test_part_2():
#     result = part_2(df=test_df_2)
#
#     assert result == None
