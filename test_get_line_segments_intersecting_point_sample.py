import math
import pickle

from geometry import get_line_segments_intersecting_point


def read(input_file='get_line_segments_intersecting_point_sample'):
    with open(f'./tests/data/{input_file}.pkl', 'rb') as f:
        rows = pickle.load(f)
    return rows


def flatten(data):
    if isinstance(data, tuple):
        if len(data) == 0:
            return ()
        else:
            return flatten(data[0]) + flatten(data[1:])
    else:
        return (data,)


def test_get_line_segments_intersecting_point_sample():
    rows = read()
    for row in rows:
        args, res = row[:-1], row[-1]
        res_hat = get_line_segments_intersecting_point(*args)
        if res_hat is None or res is None:
            assert res_hat == res, args
        elif type(res) is list:
            for r, r_hat in zip(res, res_hat):
                assert r == r_hat
        elif type(res) is tuple:
            res = flatten(res)
            res_hat = flatten(res_hat)
            for r, r_hat in zip(res, res_hat):
                assert math.isnan(r) and math.isnan(r_hat) or abs(r_hat - r) <= 0.0001, rows
        else:
            assert math.isnan(res) and math.isnan(res_hat) or abs(res_hat - res) <= 0.0001, args