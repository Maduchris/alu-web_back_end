#!/usr/bin/env python3
"""Write a type-annotated function sum_list.
"""
from typing import List

def sum_list(input_list: typing.List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
    input_list (list[float]): The input list of floats.

    Returns:
    float: The sum of the input list of floats.
    """
    return sum(input_list)
