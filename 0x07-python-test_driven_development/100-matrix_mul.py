#!/urs/bin/python3
"""Module for matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a(list of lists of ints/floats): The first matrix.
        m_b(list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        new_matrix.append([])
        for j in range(len(m_b[0])):
            new_matrix[i].append(0)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
