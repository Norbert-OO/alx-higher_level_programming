#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    
    """A function that prints the first x elements of a list and only integers.

    - Prototype: def safe_print_list_integers(my_list=[], x=0):
    - my_list can contain any type (integer, string, etc)
    - All integers have to be printed on the same line followed by a new line 
    - other type of value in the list must be skipped (in silence)
    - x represents the number of elements to access in my_list
    - x can be bigger than the length of my_list
      (if it's the case an exception is expected to occur)
    - You have to use try: /except:
    - You have to use "{:d}".format() to print an integer
    - You are not allowed to import any module
    - You are not allowed to use len()

    Return:
    The real numbers of integers printed

    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
