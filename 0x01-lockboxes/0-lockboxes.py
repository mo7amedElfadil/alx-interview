#!/usr/bin/python3
"""
Module for lockboxes challenge
Determines if all the boxes can be opened given n number of locked boxes.
Each box is numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.
Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    Initial attempt using simple list traversal.
    """
    if not boxes:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    return len(keys) == len(boxes)
