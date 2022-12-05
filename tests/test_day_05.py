from day_05 import part_1, part_2

test_data = "./data/day_05.txt"


def test_part_1():
    result = part_1(filename=test_data)

    assert result == "CMZ"


def test_part_2():
    result = part_2(filename=test_data)

    assert result == "MCD"
