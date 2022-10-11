#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len_a, len_b = len(tuple_a), len(tuple_b)
    if len_a > 1:
        a_0, a_1 = tuple_a[0], tuple_a[1]
    elif len_a == 1:
        a_0 = tuple_a[0]
        a_1 = 0

    elif len_a == 0:
        a_0, a_1 = 0, 0

    if len_b > 1:
        b_0, b_1 = tuple_b[0], tuple_b[1]
    elif len_b == 1:
        b_0 = tuple_b[0]
        b_1 = 0
    elif len_b == 0:
        b_0, b_1 = 0, 0

    return (a_0 + b_0, a_1 + b_1)
