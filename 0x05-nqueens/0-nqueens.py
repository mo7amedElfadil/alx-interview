#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
The solution utilizes backtracking to solve the problem.
"""
from sys import argv


class NQueens:
    """ Class to solve the N queens problem
        Args:
            n (int): number of queens and size of chessboard (NxN)

        Attributes:
            n (int, private): number of queens and size of chessboard (NxN)
            board (list, private): chessboard with size (NxN)
                Format: list of N lists with N elements each initialized to 0
            state (list, private): state of the board to test for solutions.
                Has a size of n. The index represents the rows and the value
                represents the column where the queen is placed.
            solutions (list, public): list of solutions/states for the puzzle.
                Satisfies conditions:
                    Every queen must not share a row, column,
                    or diagonal with any other queen.

        Methods:
            n (Public): property setter and getter.
            board (Public): property setter and getter.
            state (Public): property setter and getter.
            reset_state (Public): resets state to default value
            check_solution (staticmethod): tests if state, row and columns meet
                the solution criteria where:
                    Every queen must not share a row, column, or
                    diagonal with any other queen.

            solve_n_queens (Public): Instance method for solving the problem
                Methods:
                    backtrack (static method): recursive algorithm that
                    implements backtracking to check the solution and eliminate
                    non solutions
            print_solution (Public): Instance method that prints the solutions
    """
    def __init__(self, N):
        """ Initialize class
            Args:
                N (int): number of queens and size of chessboard (NxN)
            Properties:
                n (int): number of queens and size of chessboard (NxN)
                board (list): chessboard with size n×n
                state (list): state of the board to test for solutions.
                    Has a size of n. The index represents the rows and the
                    value represents the column where the queen is placed.
                solutions (list): list of solutions/states for the puzzle.
                    Satisfies conditions:
                        Every queen must not share a row, column,
                        or diagonal with any other queen.
        """
        self.N = N
        self.board = N
        self.reset_state()
        self.solutions = []
        self.solve_n_queens()
        self.print_solution()

    @property
    def board(self):
        """board property getter."""
        return self.__board

    @board.setter
    def board(self, N):
        """ board property setter.
            Initializes the board with zeros
            Format: list of N lists with N elements each initialized to 0 (NxN)
        """
        self.__board = [[0] * N for _ in range(N)]

    @property
    def N(self):
        """ N property getter. """
        return self.__N

    @N.setter
    def N(self, value):
        """ N property setter. """
        self.__N = value

    @property
    def state(self):
        """ state property getter. """
        return self.__state

    @state.setter
    def state(self, N):
        """ state property setter.
            Format: list of N elements
            Each element represents the column where the queen is placed
            in the corresponding row (index)
        """
        self.__state = [0] * N

    def reset_state(self):
        """ resets state to default value
        """
        self.state = self.N

    @staticmethod
    def check_solution(state, row, col):
        """ Checks the solution meets the criteria where:
            Every queen must not share a row, column, or
            diagonal with any other queen.
            Description:
                Checks if the column and diagonal positions are valid
                for the current row
                Check columns and diagonals
                Only need to check left side for columns
                and diagonals since we are moving from left to right
                and placing one queen at a time.
                For columns, we check if there is a queen in the same column
                For diagonals, the difference between the columns and the rows
                of two queens should not be equal.
        """
        for i in range(row):
            if state[i] == col or \
               state[i] - i == col - row or \
               state[i] + i == col + row:
                return False
        return True

    def solve_n_queens(self) -> None:
        """ Solves the N queens problem
            Methods:
                backtrack (static method): recursive algorithm that
                implements backtracking to check the solution and eliminate
                non solutions
        """
        def backtrack(row) -> None:
            """ Recursive algorithm that implements backtracking
                to check the solution and eliminate non solutions
                Args:
                    row (int): current row to check
                Description:
                    If the row is equal to N, a solution is found
                    and the state is appended to the solutions list
                    Otherwise, the function checks if the solution
                    meets the criteria and calls itself recursively
                    to check the next row
            """
            if row == self.N:
                self.solutions.append(self.state[:])
                return
            for col in range(self.N):
                if self.check_solution(self.state, row, col):
                    self.state[row] = col
                    backtrack(row + 1)

        self.solutions = []
        self.reset_state()
        backtrack(0)

    def print_solution(self) -> None:
        """ Instance method that prints the solutions if found
            Format: list of lists
            Each list represents a solution
            eg. [[0, 1], [1, 3], [2, 0], [3, 2]] where
            the first element in each sub list represents the row
            and the second element represents the column
        """
        if not self.solutions:
            return
        x = []
        for s, sol in enumerate(self.solutions):
            x.append([[r, c] for r, c in enumerate(sol)])
            print(x[s])


def validate_input() -> int:
    """ Validates the input from the command line is a number greater than 4
        Returns:
            int: N
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    return N


if __name__ == '__main__':
    NQueens(validate_input())
