from utilities.dataframes import get_input, load, display

DECODE = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

SHAPE = {
    'R': 1,
    'P': 2,
    'S': 3
}

WINNERS = [
    ('R', 'S'),
    ('P', 'R'),
    ('S', 'P')
]

DECODE_OUTCOME = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

def create_df(data=None):
    if not data:
        data = get_input(day="02")
    df = load(data)
    df.rename(columns={0: 'elf', 1: 'me'}, inplace=True)
    return df


def calculate_outcome(row):


    if row['elf'] == row['me']:
        return 3
    elif (row['elf'], row['me']) in WINNERS:
        return 0
    else:
        return 6


def get_total_score(df):

    df['elf'] = df['elf'].map(DECODE)
    df['me'] = df['me'].map(DECODE)


    df['shape_score'] = df['me'].map(SHAPE)


    df['outcome'] = df.apply(lambda x: calculate_outcome(row=x), axis=1)

    df['total_score'] = df['shape_score'] + df['outcome']

    return df['total_score'].sum()



def calculate_shape(row):
    if row['outcome'] == 3:
        return row['elf']
    elif row['outcome'] == 0:
        return [x[1] for x in WINNERS if x[0] == row['elf']][0]
    else:
        return [x[0] for x in WINNERS if x[1] == row['elf']][0]


def get_shapes(df):
    df['elf'] = df['elf'].map(DECODE)
    df['outcome'] = df['me'].map(DECODE_OUTCOME)

    df['my_shape'] = df.apply(lambda x: calculate_shape(row=x), axis=1)
    df['shape_score'] = df['my_shape'].map(SHAPE)
    df['total_score'] = df['shape_score'] + df['outcome']

    return df['total_score'].sum()


part1 = get_total_score(df=create_df())
print(f"Part 1: {part1}")

part2 = get_shapes(df=create_df())
print(f"Part 2: {part2}")