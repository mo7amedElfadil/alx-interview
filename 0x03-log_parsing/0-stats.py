#!/usr/bin/python3
"""
0. Log parsing
"""
import sys
from typing import Dict


def print_log(acc: Dict) -> None:
    """
    This function prints the statistics from input read
    """
    print('File size: {}'.format(acc['file_size']))
    for key, value in sorted(acc['status_code'].items()):
        if value:
            print('{}: {}'.format(key, value))


def process_line(line: str, acc: Dict) -> bool:
    """
    Processes a single log line and updates the statistics

    Parameters:
    ----------
    line: str
        The processed line
    acc: Dict
        The accumulator dictionary to update statistics

    Returns:
    -------
    bool
        True if the line was processed successfully, False otherwise
    """
    parts = line.split()
    try:
        size = int(parts[-1])
        status = int(parts[-2])
        if status in acc['status_code']:
            acc['status_code'][status] += 1
            acc['file_size'] += size
            return True
    except (IndexError, ValueError):
        return False
    return False


def main() -> None:
    """
    The entry point of the app
    """
    count = 0
    acc = {'file_size': 0,
       'status_code': {200: 0, 301: 0, 400: 0, 401: 0,
                       403: 0, 404: 0, 405: 0, 500: 0}}
    try:
        for line in sys.stdin:
            if process_line(line, acc):
                count += 1
                if count % 10 == 0:
                    print_log(acc)
        print_log(acc)
    except KeyboardInterrupt:
        print_log(acc)


if __name__ == '__main__':
    main()
