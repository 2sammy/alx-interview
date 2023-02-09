#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD

"""UTF-8 validator"""





def validUTF8(data):

    """

        Check that a sequence of byte values follows the UTF-8 encoding

        rules.  Does not check for canonicalization (i.e. overlong encodings

        are acceptable).

        """



    data = iter(data)

    for leading_byte in data:

        leading_ones = _count_leading_ones(leading_byte)

        if leading_ones in [1, 7, 8]:

            return False

        for _ in range(leading_ones - 1):

            trailing_byte = next(data, None)

            if trailing_byte is None or trailing_byte >> 6 != 0b10:

                return False

    return True





def _count_leading_ones(byte):

    """Counts the leading ones."""



    for i in range(8):

        if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:

            return i

return 8
=======
"""UTF-8 validator"""
=======
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""
from itertools import takewhile


def int_to_bits(nums):
    """
    Helper function
    Convert ints to bits
    """
    for num in nums:
        bits = []
        mask = 1 << 8  # cause we have 8 bits per byte. adds up to (11111111)
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits
>>>>>>> 26d9a55b9c22b396ed6b46a2a4c98d5780cdd180


def validUTF8(data):
    """
    Takes a list of ints and returns true if the list is
    a valid UTF-8 encoding, else returns false
    Args:
        data : List of ints representing possible UTF-8 encoding
    Return:
        bool : True or False
    """
    bits = int_to_bits(data)
    for byte in bits:
        # if single byte char, then valid. continue
        if byte[0] == 0:
            continue

        # if here, byte is multi-byte char
        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:  # UTF-8 can be 1 to 4 bytes long
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
<<<<<<< HEAD


def _count_leading_ones(byte):
    """Counts the leading ones."""

    for i in range(8):
        if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:
            return i
    return 8
>>>>>>> bccd8c6e15cbb0fea3cfcf045391094201f6a6c4
=======
>>>>>>> 26d9a55b9c22b396ed6b46a2a4c98d5780cdd180
