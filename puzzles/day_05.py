import re

import numpy as np
from utilities.defs import INPUT_DATA

DAY = "05"


def strip_line(line):
    return line.replace("\n", "").replace("[", "").replace("]", "").replace(" ", "")


def get_piles_as_dict(data):
    piles = []
    instructions = {}
    n = 4
    delim = 0
    for j, row in enumerate(data):
        d = [strip_line(line=row[i : i + n]) for i in range(0, len(row), n)]
        if row.isspace():
            delim = j + 1
        elif row[:4] == "move":
            instructions[str(j + 1 - delim)] = row.strip("\n")
        else:
            try:
                [int(x) for x in d]
            except Exception:
                piles.append(d)

    piles = fill_blanks(piles=piles)
    np_piles = np.array(piles)
    transposed_piles = np.transpose(np_piles)
    transposed_piles = np.fliplr(transposed_piles)
    piles_as_list = transposed_piles.tolist()
    final_list = []
    for x in piles_as_list:
        z = [y for y in x if y != ""]
        final_list.append(z)
    return final_list, instructions


def fill_blanks(piles):
    longest_list = max(len(item) for item in piles)
    new_piles = []
    for i, pile in enumerate(piles):
        pile_len = len(pile)
        fill = [""] * (longest_list - pile_len)
        p = pile + fill
        new_piles.append(p)
    return new_piles


def perform_instruction(piles, move, _from, to):
    for item in range(1, int(move) + 1):
        move_from = piles[_from - 1]
        move_to = piles[to - 1]
        moving = move_from.pop()
        move_to.append(moving)
    return piles


def part_1(filename):
    with open(filename) as file:
        data_by_line = file.readlines()

    piles, instructions = get_piles_as_dict(data=data_by_line)

    # print(piles)
    # print(instructions)

    for i, instruction in instructions.items():
        r = re.findall(r"\d+", instruction)
        perform_instruction(piles=piles, move=int(r[0]), _from=int(r[1]), to=int(r[2]))

    top_of_of_the_piles = "".join([x.pop() for x in piles])
    return top_of_of_the_piles

    # display(df)


def perform_multiple_instruction(piles, move, _from, to):
    move_from = piles[_from - 1]
    move_from_len = len(move_from)
    move_to = piles[to - 1]
    moving = move_from[-move:]
    move_from_remaining = move_from_len - move
    piles[_from - 1] = move_from[:move_from_remaining]
    piles[to - 1] = move_to + moving
    return piles


def part_2(filename):
    with open(filename) as file:
        data_by_line = file.readlines()

    piles, instructions = get_piles_as_dict(data=data_by_line)

    for i, instruction in instructions.items():
        r = re.findall(r"\d+", instruction)

        final_piles = perform_multiple_instruction(
            piles=piles, move=int(r[0]), _from=int(r[1]), to=int(r[2])
        )

    top_of_of_the_piles = []
    for item in final_piles:
        try:
            top_of_of_the_piles.append(item.pop())
        except Exception:
            pass

    return "".join(top_of_of_the_piles)


part1 = part_1(filename=f"{INPUT_DATA}/day05.txt")
print(f"Part 1: {part1}")

part2 = part_2(filename=f"{INPUT_DATA}/day05.txt")
print(f"Part 2: {part2}")
