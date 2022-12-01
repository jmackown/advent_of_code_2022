from day01 import get_max_total_calories, get_total_top_3, create_df

test_data = "./data/day_01_a.txt"
test_df = create_df(data=test_data)


def test_part_1():

    result = get_max_total_calories(df=test_df)

    assert result == 24000



def test_part_2():

    result = get_total_top_3(df=test_df)

    assert result == 45000