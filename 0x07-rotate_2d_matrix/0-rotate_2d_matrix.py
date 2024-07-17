#!/usr/bin/python3
""" Rotate 2D Matrix
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Do not return anything.
    The matrix must be edited in-place.
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotate 2D n x n Matrix 90 degrees clockwise
    """
    rows = len(matrix)
    """ method 1
    Transpose the matrix: Swap elements across the diagonal.
    For a given element at position (i, j), swap it with the element
    at position (j, i). Then reverse each row.

    time complexity: O(n^2)
    space complexity: O(1)
    """
    # for i in range(rows):
    #     for j in range(i, rows):
    #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # for i in range(rows):
    #     matrix[i].reverse()

    """ method 2
        Rotating concentric layers or squares layer by layer
        rotate elements in a circular fashion starting from the outermost layer

        time complexity: O(n^2)
        space complexity: O(1)

    """
    for i in range(rows // 2):
        for j in range(i, rows - i - 1):
            print(i, j)
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

    """ method 3
        Identifying left and right boundaries of current layer and rotating
        elements in a circular fashion starting from the outermost layer.
        time complexity: O(n^2)
        space complexity: O(1)
    """
    # l, r = 0, rows - 1

    # while l < r:
    #     for i in range(r - l):
    #         print(l, r, i)
    #         # save top left element
    #         topL = matrix[l][l + i]
    #         # move bottom left to top left
    #         matrix[l][l + i] = matrix[r - i][l]
    #         # move bottom right to bottom left
    #         matrix[r - i][l] = matrix[r][r - i]
    #         # move top right to bottom right
    #         matrix[r][r - i] = matrix[l + i][r]
    #         # move top left to top right
    #         matrix[l + i][r] = topL
    #     l += 1
    #     r -= 1
