#!/usr/bin/python3
def no_c(my_string):

    return ''.join(
        list(map(
            lambda letter: letter
            if letter not in ('c', 'C') else '',
            my_string
        )))
