from utilities.defs import INPUT_DATA

DAY = "06"


def part_1(filename, marker_len):
    with open(filename) as file:
        data = file.read()

    position = 0
    for i, x in enumerate(data):
        pos = int(i + 1)
        if pos < marker_len:
            pass
        else:
            group = data[pos - marker_len : pos]
            group_as_list = list(group)
            # print(f"pos: {pos}, group: {group}, list: {group_as_list}, set: {set(group_as_list)}")
            if len(set(group_as_list)) < marker_len:
                pass
            else:
                position = pos
                break
    return position


part1 = part_1(filename=f"{INPUT_DATA}/day{DAY}.txt", marker_len=4)
print(f"Part 1: {part1}")

part2 = part_1(filename=f"{INPUT_DATA}/day{DAY}.txt", marker_len=14)
print(f"Part 2: {part2}")
