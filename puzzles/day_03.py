import string

from utilities.dataframes import create_df, display, get_input, load

DAY = "03"


PRIORITY_MAPPING = {
    c: i + 1
    for i, c in enumerate(list(string.ascii_lowercase) + list(string.ascii_uppercase))
}


def split_in_half(data):
    halfway = int(len(data) / 2)
    return [data[:halfway], data[halfway:]]


def get_common_elements(data):

    # strong assumption here that there will only be one common element
    return list(set(data[0]).intersection(data[1]))[0]


def part_1(df):
    df.rename(columns={0: "contents"}, inplace=True)

    df["compartments"] = df.apply(lambda x: split_in_half(data=x["contents"]), axis=1)
    df["common"] = df.apply(
        lambda x: get_common_elements(data=x["compartments"]), axis=1
    )
    df["score"] = df["common"].map(PRIORITY_MAPPING)

    display(df)

    return df["score"].sum()


def get_more_common_elements(x):
    contents = x.to_list()
    common = set.intersection(*map(set, contents))

    return list(common)[0]


def part_2(df):
    df.rename(columns={0: "contents"}, inplace=True)
    df["every_3rd"] = df[::3]
    df["group"] = df["every_3rd"].notnull().cumsum()
    df = df.groupby("group")["contents"].apply(get_more_common_elements).reset_index()

    df["score"] = df["contents"].map(PRIORITY_MAPPING)

    display(df)

    return df["score"].sum()


part1 = part_1(df=create_df(day=DAY))
print(f"Part 1: {part1}")


part2 = part_2(df=create_df(day=DAY))
print(f"Part 2: {part2}")
