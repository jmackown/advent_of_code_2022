from day03 import sum_priorities, create_df

test_data = "./data/day_03.txt"
test_df = create_df(data=test_data)



def test_sum_priorities():
    result = sum_priorities(df=test_df)

    assert result == 157