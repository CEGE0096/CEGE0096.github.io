import math
import pickle

from geometry import is_line_horizontal


def read(input_file='is_line_horizontal_sample'):
    with open(f'./tests/data/{input_file}.pkl', 'rb') as f:
        rows = pickle.load(f)
    return rows


def test_is_line_horizontal_sample():
    rows = read()
    for row in rows:
        args, res = row[:-1], row[-1]
        res_hat = is_line_horizontal(*args)
        if type(res) is tuple:
            for r, r_hat in zip(res, res_hat):
                assert math.isnan(r) and math.isnan(r_hat) or r_hat == r, args
        else:
            assert math.isnan(res) and math.isnan(res_hat) or res_hat == res, args