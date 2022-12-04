from utilities.dataframes import create_df, display

DAY = "04"
df = create_df(day=DAY)


def part_1(df):
    df[["elf_1", "elf_2"]] = df[0].str.split(",", expand=True)
    for col in ["elf_1", "elf_2"]:
        df[col] = df.apply(
            lambda x: [
                i
                for i in range(int(x[col].split("-")[0]), int(x[col].split("-")[1]) + 1)
            ],
            axis=1,
        )

    df["2_is_in_1"] = df.apply(
        lambda x: all(elem in x["elf_1"] for elem in x["elf_2"]), axis=1
    )
    df["1_is_in_2"] = df.apply(
        lambda x: all(elem in x["elf_2"] for elem in x["elf_1"]), axis=1
    )
    df["overlap"] = df.apply(
        lambda x: True if x["2_is_in_1"] or x["1_is_in_2"] else False, axis=1
    )

    # display(df)

    return df["overlap"].sum()


def part_2(df):
    # display(df)
    pass


part1 = part_1(df=df)
print(f"Part 1: {part1}")

part2 = part_2(df=df)
print(f"Part 2: {part2}")
