from using_pytest import __version__

import random
from typing import List

from using_pytest.main import return_sum, return_same_data_type, main


def test_version():
    """Test the current version"""
    assert __version__ == '0.1.0'


def test_return_sum_triplet():
    """Test whether the test function properly returns the sum of list argument"""
    numbers = [33, 23, 13]
    assert return_sum(numbers) == 69


def test_return_sum_float_values():
    floats = [45.2, 12.3, 1.5]
    total: float = 0.0
    for number in floats:
        total += number
    assert return_sum(floats) == total


def test_if_main_returns_word():
    """Make sure that main function returns the string 'word'"""
    assert main() == 'word'


def test_return_sum_random_list_size():
    """Test list of random values and size on return_sum function"""
    outbound_list: List = []
    total: int = 0
    number_of_elements: int = random.randint(0, 100)
    for number in range(number_of_elements):
        current_number = random.randint(0, 100)
        outbound_list.append(current_number)
        total += current_number
    assert return_sum(outbound_list) == total


def test_return_same_data_type():
    """Test whether function returns the same datatype as what was supplied to it"""
    whatever: bool = True
    assert return_same_data_type(whatever)




