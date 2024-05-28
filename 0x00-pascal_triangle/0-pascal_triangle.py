#!/usr/bin/python3
"""Pascal's Triangle
Task: 0. Pascal's Triangle
Create a function
def pascal_triangle(n):
that returns a list of lists of integers representing the
Pascal’s triangle of n :
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


def pascal_triangle(n) -> list:
    """
    creates a pascal triangle represented in a list of lists.
    n represents number of rows. n lists are returned. if n <= 0,
    return an empty list
    """
    res = []
    if n <= 0:
        return res
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
