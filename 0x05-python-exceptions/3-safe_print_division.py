#!/usr/bin/python3

def safe_print_division(a, b):
    """
    A function that divides 2 integers and prints the result.
    - Prototype: def safe_print_division(a, b):
    - You can assume that a and b are integers
    - The result of the division should print on the finally: section preceded by Inside result:
    - You have to use try: / except: / finally:
    - You have to use "{}".format() to print the result.
    - You are not allowed to import any module.

    Return:
    The value of the division, Otherwise: None

    """
    result = 0
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
