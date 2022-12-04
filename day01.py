from utilities.dataframes import get_input, load


def create_df(data=None):
    if not data:
        data = get_input(day="01")
    df = load(data)
    df["elf"] = df.isnull().all(axis=1).cumsum() + 1
    df = df.dropna()
    df.rename(columns={0: "raw_data"}, inplace=True)
    return df


def get_max_total_calories(df):
    totals = df.groupby("elf")["raw_data"].sum()
    return int(totals.max())


def get_total_top_3(df):
    totals = df.groupby("elf")["raw_data"].sum()
    top3 = totals.sort_values(ascending=False).iloc[:3]

    return int(top3.sum())


part1 = get_max_total_calories(df=create_df())
print(f"Part 1: {part1}")

part2 = get_total_top_3(df=create_df())
print(f"Part 2: {part2}")
