#!/usr/bin/python3
'''module to carry out matrix multiplication'''


def matrix_mul(m_a, m_b):
    '''multiplies two matrices
    Args:
        m_a(2-D list): first matrix
        m_b(2-D list): second matrix
    Return:
        result matrix
    '''
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for vec in m_a:
        if type(vec) is not list:
            raise TypeError("m_a must be a list of lists")
    for vec in m_b:
        if type(vec) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        for item in m_a[i]:
            if type(item) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if i + 1 < len(m_a) and len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        for item in m_b[i]:
            if type(item) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if i + 1 < len(m_b) and len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("each row of m_b must be of the same size")

    product = []
    k = 0
    transposed = list(zip(*m_b))
    for vec in m_a:
        mul_list = []
        for j in range(len(transposed)):
            if len(vec) != len(transposed[j]):
                raise ValueError("m_a and m_b can't be multiplied")
            mul = 0
            for i in range(len(transposed[j])):
                mul += vec[i] * transposed[j][i]
            mul_list.append(mul)
        product.append(mul_list)

    return product
