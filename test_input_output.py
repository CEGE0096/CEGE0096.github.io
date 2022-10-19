"""
This is a test file for pytest.
If you have implemented a certain functionality,
	please change 'checklist.json' file accordingly with either 'yes' and 'no'.
"""
import json
import pandas as pd
import pytest
import os
from geometry import Point, Polygon
from algorithm import PiPAlgorithm

BASE_URL = "https://CEGE0096.github.io/"
mbr_mark_gained = 0
rca_mark_gained = 0
csv_mark_gained = 0
# TODO: Align the weight with the actual coursework marking scheme
mbr_weight, rca_weight, csv_weight = 0.2, 0.4, 0.05

# functions
mbr = PiPAlgorithm().mbr
rca = PiPAlgorithm().rca

with open(os.path.join(os.getcwd(), 'checklist.json'), 'r') as f:
	checklist = json.load(f)

with open(os.path.join(os.getcwd(), 'mark.txt'), 'w') as fp:
	fp.write(f"Student Number: {checklist['studentNumber']}\n")


@pytest.mark.skipif(checklist['MBR'] == 'no', reason="MBR is not implemented by student yet, or RCA is implemented.")
def test_mbr():
	global mbr_mark_gained
	try:
		# make input_points
		input_csv = pd.read_csv(BASE_URL + "mbr_input.csv")
		input_xs, input_ys = list(input_csv['x']), list(input_csv['y'])
		input_points = []
		for x, y in zip(input_xs, input_ys):
			point = Point(x, y)
			input_points.append(point)

		# make polygon
		polygon_csv = pd.read_csv(BASE_URL + "polygon.csv")
		polygon_xs, polygon_ys = list(polygon_csv['x']), list(polygon_csv['y'])
		polygon_points = []
		for x, y in zip(polygon_xs, polygon_ys):
			point = Point(x, y)
			polygon_points.append(point)
		polygon = Polygon(polygon_points)

		# compute with your mbr algo
		results = []
		for input_point in input_points:
			result = mbr(input_point, polygon)
			results.append(result)

		# get ground truth results
		gt_output_csv = pd.read_csv(BASE_URL + "mbr_output.csv")
		gt_outputs = list(gt_output_csv['category'])

		assert results == gt_outputs
		mbr_mark_gained = 100

	except AssertionError:
		for res, gt in zip(results, gt_outputs):
			if res == gt:
				mbr_mark_gained += 1
	except Exception:
		mbr_mark_gained = 0
	finally:
		with open('./mark.txt', 'a') as fp:
			fp.write(f"MBR mark: {mbr_mark_gained}/100\n")


@pytest.mark.skipif(checklist['RCA'] == 'no', reason="RCA is not implemented by student yet.")
def test_rca():
	try:
		global rca_mark_gained
		# make input_points
		input_csv = pd.read_csv(BASE_URL + "rca_complete_input.csv")
		input_xs, input_ys = list(input_csv['x']), list(input_csv['y'])
		input_points = []
		for x, y in zip(input_xs, input_ys):
			point = Point(x, y)
			input_points.append(point)

		# make polygon
		polygon_csv = pd.read_csv(BASE_URL + "polygon.csv")
		polygon_xs, polygon_ys = list(polygon_csv['x']), list(polygon_csv['y'])
		polygon_points = []
		for x, y in zip(polygon_xs, polygon_ys):
			point = Point(x, y)
			polygon_points.append(point)
		polygon = Polygon(polygon_points)

		# compute with your rca_complete algo
		results = []
		for input_point in input_points:
			result = rca(input_point, polygon)
			results.append(result)

		# get ground truth results
		gt_output_csv = pd.read_csv(BASE_URL + "rca_complete_output.csv")
		gt_outputs = list(gt_output_csv['category'])

		assert results == gt_outputs
		rca_mark_gained = 100

	except AssertionError:
		for res, gt in zip(results, gt_outputs):
			if res == gt:
				rca_mark_gained += 1
	except Exception:
		rca_mark_gained = 0
	finally:
		with open('./mark.txt', 'a') as fp:
			fp.write(f"RCA mark: {rca_mark_gained}/100\n")


@pytest.mark.skipif(checklist['RCA'] == 'no' or checklist['MBR'] == 'no', reason="Algorithms are not implemented.")
def test_csv():
	global csv_mark_gained
	gt_output_csv = pd.read_csv(BASE_URL + "rca_complete_output.csv")
	gt_outputs = list(gt_output_csv['category'])

	try:
		my_csv = pd.read_csv(os.path.join(os.getcwd(), 'output.csv'))
		my_outputs = list(my_csv['category'])
		my_id = list(my_csv['id'])

		assert my_id == [i for i in range(1, 101)]
		assert my_outputs == gt_outputs
		csv_mark_gained = 100

	except FileNotFoundError or KeyError or AssertionError:
		csv_mark_gained = 0
	finally:
		with open('./mark.txt', 'a') as fp:
			fp.write(f"CSV mark: {csv_mark_gained}/100\n\n")
			fp.write(f"Weight of each component: MBR={mbr_weight} ; RCA={rca_weight} ; CSV={csv_weight}\n")
			fp.write(f"Total mark gained from coding: "
					 f"{round(mbr_weight * mbr_mark_gained + rca_weight * rca_mark_gained + csv_weight * csv_mark_gained, 2)}"
					 f" / 100\n\n")
			fp.write("Rest of the mark will be decided by marking your report")
			fp.close()
