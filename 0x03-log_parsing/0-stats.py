#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics about
status codes count and total file size
"""
import sys


codes = {}
size = 0
limit = 0
try:
    for line in sys.stdin:
        try:
            intel = line.split(" ")
            size += int(intel[-1])
            if len(intel[-2]) == 3:
                codes[int(intel[-2])] = codes.get(int(intel[-2]), 0) + 1
                limit += 1
        except (IndexError, ValueError):
            pass
        if limit == 10:
            limit = 0
            print("File size: {}".format(size))
            for key, value in sorted(codes.items()):
                print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(size))
    for key, value in sorted(codes.items()):
        print("{}: {}".format(key, value))
