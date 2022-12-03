import string

import pandas as pd

from utilities.dataframes import get_input, load, display


PRIORITY_MAPPING = {c: i+1 for i, c in enumerate(list(string.ascii_lowercase) + list(string.ascii_uppercase))}


def create_df(data=None):
    if not data:
        data = get_input(day="03")
    df = load(data)
    df.rename(columns={0: 'contents'}, inplace=True)
    return df

def split_in_half(data):
    halfway = int(len(data)/2)
    return [data[:halfway], data[halfway:]]

def get_common_elements(data):

    # strong assumption here that there will only be one common element
    return list(set(data[0]).intersection(data[1]))[0]

def sum_priorities(df):



    df['compartments'] = df.apply(lambda x: split_in_half(data=x['contents']), axis=1)
    df['common'] = df.apply(lambda x: get_common_elements(data=x['compartments']), axis=1)
    df['score'] = df['common'].map(PRIORITY_MAPPING)

    display(df)

    return df['score'].sum()


part1 = sum_priorities(df=create_df())
print(f"Part 1: {part1}")