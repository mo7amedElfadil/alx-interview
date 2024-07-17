#!/usr/bin/python3
""" Rotate 2D Matrix
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Do not return anything.
    The matrix must be edited in-place.
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate 2D n x n Matrix 90 degrees clockwise
        Rotating concentric layers or squares layer by layer
        rotate elements in a circular fashion starting from the outermost layer

        time complexity: O(n^2)
        space complexity: O(1)

    """
    rows = len(matrix)
    for i in range(rows // 2):
        for j in range(i, rows - i - 1):
            # save top left element
            temp = matrix[i][j]
            # move bottom left to top left
            matrix[i][j] = matrix[rows - 1 - j][i]
            # move bottom right to bottom left
            matrix[rows - 1 - j][i] = matrix[rows - 1 - i][rows - 1 - j]
            # move top right to bottom right
            matrix[rows - 1 - i][rows - 1 - j] = matrix[j][rows - 1 - i]
            # move top left to top right
            matrix[j][rows - 1 - i] = temp
