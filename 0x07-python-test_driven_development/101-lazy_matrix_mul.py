#!/usr/bin/python3
"""Module for lazy_matrix_mul function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices
        Args:
            m_a (list): first matrix
            m_b (list): second matrix.
        Returns:
            list: product of m_a and m_b
    """
    return np.matmul(m_a, m_b)
