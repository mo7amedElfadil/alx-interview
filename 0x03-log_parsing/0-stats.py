#!/usr/bin/python3
"""Module 101-stats:
    Processes input in the format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> \
               , defaultdict <file size>
    Every 10 lines and after a keyboard interruption (CTRL + C),
    it prints statistics:
        - Total file size: File size: <total size>
            which is the sum of all previous sizes (see input format above)
        - Number of lines by status code:
            Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
            Format: <status code>: <number>
            Status codes should be printed in ascending order.
"""
from typing import Dict, List, Tuple


def print_stats(df: Dict[int, int], size: int) -> None:
    """Prints the statistics from stdin according to the format.
    """
    print("File size: {size}".format(size=size))
    for k, v in df.items():
        if v:
            print("{k}: {v}".format(k=k, v=v))


def init_vars() -> Tuple[Dict[int, int], Dict[str, int]]:
    """Initializes the variables to be used in the program.
    """
    accumulator = {'size': 0, 'count': 0}
    df = dict.fromkeys([200, 301, 400, 401,
                        403, 404, 405, 500],
                       0)
    return df, accumulator


def update_dict(line: str, df: Dict, accumulator: Dict[str, int]) -> None:
    """Updates the dictionary and counts based on the input line.
        Every 10 lines, it prints the statistics.
    """
    parts = line.split()
    try:
        accumulator['size'] += int(parts[-1])
        if int(parts[-2]) in df:
            df[int(parts[-2])] += 1
            accumulator['count'] += 1
    except (IndexError, ValueError):
        pass
    if accumulator['count'] % 10 == 0:
        print_stats(df, accumulator['size'])


def update_stats() -> None:
    """Reads lines from stdin and updates the statistics accordingly.
        Prints the statistics every 10 lines and on keyboard interruption.
    """
    from sys import stdin
    df, accumulator = init_vars()
    try:
        for line in stdin:
            update_dict(line, df, accumulator)
        print_stats(df, accumulator['size'])
    except KeyboardInterrupt:
        print_stats(df, accumulator['size'])


if __name__ == "__main__":
    update_stats()
