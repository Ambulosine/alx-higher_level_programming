#!/usr/bin/python3
'''module that contain a function that divides all elements of a
matrix by a given number'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix by div
    Args:
        matrix(2-D list): the matrix
        div(int): the divisor
    Return:
        2-D list: matrix of the result of division
    '''
    mat_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(mat_err)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    res_matrix = []
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(mat_err)
        if i < len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

        res_row = []
        for k in range(len(matrix[i])):
            if type(matrix[i][k]) not in [int, float]:
                raise TypeError(mat_err)
            res = round(matrix[i][k] / div, 2)
            res_row.append(res)

        res_matrix.append(res_row)

    return res_matrix
