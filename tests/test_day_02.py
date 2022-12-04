from day02 import create_df, get_shapes, get_total_score

test_data = "./data/day_02.txt"
test_df = create_df(data=test_data)


def test_get_total_score():

    expected_result = 15

    result = get_total_score(df=test_df)

    assert result == expected_result


def test_get_shapes():
    result = get_shapes(df=test_df)

    assert result == 12
