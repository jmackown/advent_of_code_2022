from day_{{day}} import part_1, part_2

from utilities.dataframes import load

test_data = "./data/day_{{day}}.txt"
test_df_1 = load(filename=test_data)
test_df_2 = load(filename=test_data)



def test_part_1():
    result = part_1(df=test_df_1)

    assert result == None


def test_part_2():
    result = part_2(df=test_df_2)

    assert result == None
