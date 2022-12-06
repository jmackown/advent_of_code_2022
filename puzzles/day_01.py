from utilities.dataframes import create_df

DAY = "01"


def part_1(df):
    df["elf"] = df.isnull().all(axis=1).cumsum() + 1
    df = df.dropna()
    df.rename(columns={0: "raw_data"}, inplace=True)

    totals = df.groupby("elf")["raw_data"].sum()
    return int(totals.max())


def part_2(df):
    df["elf"] = df.isnull().all(axis=1).cumsum() + 1
    df = df.dropna()
    df.rename(columns={0: "raw_data"}, inplace=True)
    totals = df.groupby("elf")["raw_data"].sum()
    top3 = totals.sort_values(ascending=False).iloc[:3]

    return int(top3.sum())


part1 = part_1(df=create_df(day=DAY))
print(f"Part 1: {part1}")

part2 = part_2(df=create_df(day=DAY))
print(f"Part 2: {part2}")
