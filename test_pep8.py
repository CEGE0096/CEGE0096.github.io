# install pip install flake8 pep8-naming
import os
import re
import pytest

pytest.flake8_codes = None


def run_flake8():
    files = ['files.py', 'geometry.py', 'main.py', 'miscellaneous.py']
    os.system(f"flake8 --statistics -qq {' '.join(files)} > flake8_output")
    with open('flake8_output', 'r') as f:
        flake8_output = f.read()
        # assign the set to the global flake8_codes
        pytest.flake8_codes = set(re.findall('([A-Z][0-9][0-9][0-9])', flake8_output))
    os.system('rm flake8_output')


def test_function_names():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'N802' not in pytest.flake8_codes


def test_variable_names():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'N806' not in pytest.flake8_codes


def test_variable_assigned_but_never_used():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'F841' not in pytest.flake8_codes


def test_class_variable_names():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'N801' not in pytest.flake8_codes


def test_first_argument_classes():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'N805' not in pytest.flake8_codes


def test_function_names_underscores():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'N807' not in pytest.flake8_codes


def test_blank_line_end_file():
    if pytest.flake8_codes is None:
        run_flake8()
    assert 'W391' not in pytest.flake8_codes
