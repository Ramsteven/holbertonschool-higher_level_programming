#!/usr/bin/python3
"""
This is the module for
    matrix_divided function

"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    new_list = []
    row_list = []
    tmp_column = 0
    i = 0

    handle_matrix = isinstance(matrix, (list)) and len(matrix) != 0
    handle_div = isinstance(div, (int, float))

    if handle_matrix is False or handle_div is False:
        raise TypeError("{}"
                        .format("matrix must be a matrix (list of lists)\
 of integers/floats" if handle_matrix is False else "div must be a number"))

    if type(div) == 0:
        raise ZeroDivisionError("division by zero")

    for column in matrix:
        row_list = []
        if type(column) is not list and len(column) == 0:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        if i != 0:
            if len(matrix[i - 1]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must\
 have the same size")
        for row in column:
            if isinstance(row, (int, float)) is True:
                division = float("{:.2f}".format(row/div))
            else:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            row_list.append(division)
        i += 1
        new_list.append(row_list)
    return new_list
