# install pip install flake8 pep8-naming
import os
import re


def get_flake8_codes():
    os.system('flake8 --statistics -qq . > flake8_output')
    with open('flake8_output', 'r') as f:
        flake8_output = f.read()
        codes = set(re.findall('([A-Z][0-9][0-9][0-9])', flake8_output))
    os.system('rm flake8_output')
    return codes


def test_function_names():
    assert 'N802' not in get_flake8_codes()


def test_variable_names():
    assert 'N806' not in get_flake8_codes()


def test_variable_assigned_but_never_used():
    assert 'F841' not in get_flake8_codes()


def test_class_variable_names():
    assert 'N801' not in get_flake8_codes()


def test_first_argument_classes():
    assert 'N805' not in get_flake8_codes()


def test_function_names_underscores():
    assert 'N807' not in get_flake8_codes()


def test_blank_line_end_file():
    assert 'W391' not in get_flake8_codes()
