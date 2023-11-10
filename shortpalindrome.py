#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the short_palindrome_count function below.
def short_palindrome_count(s):
    mod = 10**9 + 7
    # Arrays to store count of characters and pairs of characters
    char_count = [0] * 26
    pair_count1 = [0] * 26 * 26
    pair_count2 = [0] * 26 * 26
    total_count = 0
    indices_26 = list(range(26))

    for char in s:
        char_index = ord(char) - 97
        pair_index1 = 26 * char_index - 1
        pair_index2 = char_index - 26

        # Update total count using the counts in pair_count2
        total_count += pair_count2[pair_index2]

        # Update pair_count2 using the counts in pair_count1
        pair_count2[pair_index1] += pair_count1[pair_index1]

        # Update pair_count1 using the counts in char_count
        pair_count1[pair_index1] += char_count[char_index]

        # Update char_count
        char_count[char_index] += 1

    return total_count % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = short_palindrome_count(s)

    fptr.write(str(result) + '\n')

    fptr.close()
