#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid) -> int:
    """
        Function that returns the perimeter of the island described in grid
        Args:
            grid: List of list of integers
        Return:
            The perimeter of the island
    """
    def node_perimeter(r: int, c: int,
                       rows: int, cols: int) -> int:
        """
            Function that returns the perimeter of a node
            Args:
                grid: List of list of integers
                r: integer (row position)
                c: integer (column position)
                rows: integer (number of rows)
                cols: integer (number of columns)
            Return:
                The perimeter of the node
        """
        perimeter = 0
        if r == 0 or grid[r - 1][c] == 0:
            perimeter += 1
        if r == rows - 1 or grid[r + 1][c] == 0:
            perimeter += 1
        if c == 0 or grid[r][c - 1] == 0:
            perimeter += 1
        if c == cols - 1 or grid[r][c + 1] == 0:
            perimeter += 1
        return perimeter

    total = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                total += node_perimeter(r, c, rows, cols)
    return total
