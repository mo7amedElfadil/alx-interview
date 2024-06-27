#!/usr/bin/env python3
"""Validate UTF-8
    - A valid UTF-8 character can be 1 - 4 bytes long
    - For a 1-byte character, the first bit is a 0, followed by its unicode
      code
    - For an n-byte character, the first n-bits are all 1, the n+1 bit is 0,
      followed by n-1 bytes with most significant 2 bits being 10
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding
    Description:
        - Iterate through each byte in the input data.
        - Check if the bytes conform to the UTF-8 encoding rules,
            including correct leading bits for starting bytes and correct
            format for continuation bytes.
        - Returns True if all bytes form valid UTF-8 characters,
            otherwise return False.
    Args:
        data: list of integers
    Returns:
        True if data is a valid UTF-8 encoding, else return False

    """
    num_bytes = 0  # number of bytes in the current UTF-8 character

    for byte in data:  # iterate over each byte in data

        mask = 1 << 7  # init mask to 0b10000000 i.e 128
        """
            if num_bytes is 0, then we are looking for the start of
            a new UTF-8 character
        """
        if num_bytes == 0:
            while mask & byte:  # check if the byte is a start of UTF-8 char
                # each time the leading bit is 1, increment num_bytes
                num_bytes += 1  # incr the number of bytes in the UTF-8 char
                mask = mask >> 1  # shift mask to right by 1 to check next bit
            """
                After checking the leading bits and num_bytes is still 0
                it means the byte represents a single byte character
                i.e ASCII character (0xxxxxxx) so we continue to the next byte
            """
            if num_bytes == 0:
                continue

            """
                If num_bytes is 1 or greater than 4, it is invalid UTF-8:
                num_bytes == 1 means the byte starts with 10xxxxxx,
                which is not valid for the start of a character.
                num_bytes > 4 exceeds the maximum length of a UTF-8 character
                (which is 4 bytes).
            """
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            """
                If num_bytes is greater than 0, the function expects
                continuation bytes:
                Continuation bytes should follow the format 10xxxxxx.
                The byte is checked to ensure the two most significant
                bits are 10.
                If the check fails, the function returns False.
            """
            if not (byte & 1 << 7 and not (byte & 1 << 6)):
                return False
        num_bytes -= 1  # decrement num_bytes after checking each byte
    """
        After processing all bytes, the function returns True if
        num_bytes is 0, indicating that all characters were properly completed.
        If num_bytes is not 0, it means there were incomplete characters,
        and the function returns False.
    """
    return num_bytes == 0
