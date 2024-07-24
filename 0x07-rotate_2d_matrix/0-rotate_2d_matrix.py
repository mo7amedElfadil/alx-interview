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
    print("Method 1")
    for i in range(rows):
        for j in range(i, rows):
            print(f"i: {i}, j: {j}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(rows):
        matrix[i].reverse()


def rotate_2d_matrix_v1(matrix) -> None:
    """ method 2
        Rotating concentric layers or squares layer by layer
        rotate elements in a circular fashion starting from the outermost layer

        time complexity: O(n^2)
        space complexity: O(1)

    """
    print("Method 2")
    rows = len(matrix)
    r = rows - 1
    for i in range(rows // 2):
        for j in range(i, r - i):
            print(f"i: {i}, j: {j}")
            # save top left element
            temp = matrix[i][j]
            # move bottom left to top left
            matrix[i][j] = matrix[r - j][i]
            # move bottom right to bottom left
            matrix[r - j][i] = matrix[r - i][r - j]
            # move top right to bottom right
            matrix[r - i][r - j] = matrix[j][r - i]
            # move top left to top right
            matrix[j][r - i] = temp


def rotate_2d_matrix_v2(matrix) -> None:
    """ method 3
        Identifying left and right boundaries of current layer and rotating
        elements in a circular fashion starting from the outermost layer.
        time complexity: O(n^2)
        space complexity: O(1)
    """
    rows = len(matrix)
    l, r = 0, rows - 1
    print("Method 3")

    while l < r:
        for i in range(r - l):
            print(f"i: {i} l: {l} r: {r}")
            top = l
            bottom = r
            # save top left element
            topL = matrix[top][l + i]
            # move bottom left to top left
            matrix[top][l + i] = matrix[bottom - i][l]
            # move bottom right to bottom left
            matrix[r - i][l] = matrix[r][r - i]
            # move top right to bottom right
            matrix[r][r - i] = matrix[l + i][r]
            # move top left to top right
            matrix[l + i][r] = topL
        l += 1
        r -= 1


if __name__ == "__main__":
    # m1 4 x 4
    m1 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
    m2 = m1.copy()
    m3 = m1.copy()
    rotate_2d_matrix(m1)
    rotate_2d_matrix_v1(m2)
    rotate_2d_matrix_v2(m3)

