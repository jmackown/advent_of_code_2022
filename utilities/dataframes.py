
import os

import pandas as pd
from tabulate import tabulate


def load(filename):
    df = pd.read_csv(filename, sep=" ", header=None, skip_blank_lines=False)
    df.rename(columns={0: 'raw_data'}, inplace=True)
    return df


def display(df):
    print(f"\n{tabulate(df, headers='keys', tablefmt='psql')}")


def get_input(day):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f'input_data/day{day}.txt')