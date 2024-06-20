#!/usr/bin/python3
"""
0. Log parsing
"""
import sys

acc = {'file_size': 0,
       'status_code': {200: 0, 301: 0, 400: 0, 401: 0,
                       403: 0, 404: 0, 405: 0, 500: 0}}


def print_log():
    """
    This function prints the statistics from input read
    """
    print('File size: {}'.format(acc['file_size']))
    for key, v in acc['status_code'].items():
        if v:
            print('{}: {}'.format(key, v))


def processer(line):
    """
    This is the main engine which process the lines read

    Parameters:
    ----------
    line: str
        The processed line
    """
    size = line.split()[-1]
    status = line.split()[-2]
    if int(status) in list(acc['status_code'].keys()):
        acc['status_code'][int(status)] += 1
        acc['file_size'] += int(size)
        return True
    return False


def main():
    """
    The entry point of the app
    """
    count = 0
    try:
        for line in sys.stdin:
            if processer(line):
                count += 1
            if (count % 10 == 0):
                print_log()
        print_log()
    except KeyboardInterrupt:
        print_log()


if __name__ == '__main__':
    main()
