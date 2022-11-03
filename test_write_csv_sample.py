import filecmp
import math
import pickle

from files import write_csv


def read(input_file='write_csv_sample'):
    with open(f'./tests/data/{input_file}.pkl', 'rb') as f:
        rows = pickle.load(f)
    return rows

def test_write_csv_sample():
    rows = read()
    for row in rows:
        args, res = row[:-1], row[-1]
        write_csv(*args)
        assert filecmp.cmp(args[0], './tests/data/write_csv.csv')
