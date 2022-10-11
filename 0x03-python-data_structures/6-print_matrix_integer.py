#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            print("{:s}{:d}".format('' if row.index(item) == 0
                                    else ' ',
                                    int(item)),
                end='')
        print()
