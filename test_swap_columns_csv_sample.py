import filecmp
import math
import pickle

from files import swap_columns_csv


def read(input_file='swap_columns_csv_sample'):
    with open(f'./tests/data/{input_file}.pkl', 'rb') as f:
        rows = pickle.load(f)
    return rows

def test_swap_columns_csv_sample():
    rows = read()
    for row in rows:
        args, res = row[:-1], row[-1]
        swap_columns_csv(*args)
        assert filecmp.cmp(args[0], './tests/data/swap_columns_csv.csv')
