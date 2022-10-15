#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for a square class with private args

Example:
    This module is expected to have a class with private args
        $ ./1-main.py
        <class '1_square.Square'>
        {'_square__size': 3}
        'Square' object has no attribute 'size'
        'Square' object has no attribute '__size"
"""


class Square:
    """A class Square that defines a square by
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
    """

    def __init__(self, size):
        """Initialization of a square

        Args:
            __size (int): length or width should be equal and private
        """
        self.__size = size
