import math
import os
import random
import re
import sys

#
# Complete the 'find_virus_indices' function below.
#
# The function accepts following parameters:
#  1. STRING original_string
#  2. STRING virus_string
#
def small_match(substring1, substring2):
    # Check if two substrings have at most one differing character
    counter = 0
    for i in range(len(substring1)):
        if substring1[i] != substring2[i]:
            counter += 1
            if counter > 1:
                return 0
    return 1


def match(substring1, substring2):
    # Recursive function to check if two substrings match
    length = len(substring1)
    if length < 10:
        return small_match(substring1, substring2)
    
    # Split substrings into two halves
    half1_1 = substring1[:length // 2]
    half1_2 = substring1[length // 2:]
    half2_1 = substring2[:length // 2]
    half2_2 = substring2[length // 2:]

    # Check if corresponding halves match
    s1 = (half1_1 == half2_1)
    s2 = (half1_2 == half2_2)

    # Recursively check the matching of remaining halves
    if s1 and s2:
        return True
    elif s1 and not s2:
        return match(half1_2, half2_2)
    elif not s1 and s2:
        return match(half1_1, half2_1)
    else:
        return False


def find_virus_indices(original_string, virus_string):
    result = ''
    if len(virus_string) > len(original_string):
        return "No Match!"
    else:
        # Iterate through all possible substrings of original string
        for i in range(len(original_string) - len(virus_string) + 1):
            substring = original_string[i:i + len(virus_string)]

            # Check if the substring matches the virus string
            flag = match(substring, virus_string)
            if flag:
                result += str(i) + ' '
        
        # Check if any matches were found
        if len(result) == 0:
            return "No Match!"
        else:
            return result.strip()

if __name__ == '__main__':
    test_cases = int(input().strip())

    for _ in range(test_cases):
        input_strings = input().rstrip().split()

        original_str = input_strings[0]
        virus_str = input_strings[1]

        print(find_virus_indices(original_str, virus_str))
