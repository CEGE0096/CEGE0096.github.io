import math
import pickle

from geometry import are_points_equal


def read(input_file='are_points_equal_sample'):
    with open(f'./tests/data/{input_file}.pkl', 'rb') as f:
        rows = pickle.load(f)
    return rows


def test_are_points_equal_sample():
    rows = read()
    for row in rows:
        args, res = row[:-1], row[-1]
        res_hat = are_points_equal(*args)
        if res_hat is None or res is None:
            assert res_hat == res, args
        elif type(res) is tuple:
            for r, r_hat in zip(res, res_hat):
                assert math.isnan(r) and math.isnan(r_hat) or abs(r_hat - r) <= 0.0001, args
        else:
            assert math.isnan(res) and math.isnan(res_hat) or abs(res_hat - res) <= 0.0001, args