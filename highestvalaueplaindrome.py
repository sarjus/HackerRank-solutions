import math
import os
import random
import re
import sys

# Complete the highest_value_palindrome function below.
def highest_value_palindrome(s, n, k):
    min_changes_required = 0

    # Count the minimum number of changes needed to make the string a palindrome.
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            min_changes_required += 1

    # If the required changes are more than the available opportunities, it's not possible.
    if min_changes_required > k:
        return '-1'

    highest_value_palindrome = ''
    for i in range(n // 2):
        # If there are more than one change opportunities and characters are not the same, make them '9'.
        if k - min_changes_required > 1:
            if s[i] != s[n - i - 1]:
                if s[i] != '9' and s[n - i - 1] != '9':
                    highest_value_palindrome += '9'
                    k -= 2
                else:
                    # Choose the maximum value character to maximize the overall value.
                    if s[i] > s[n - i - 1]:
                        highest_value_palindrome += s[i]
                    else:
                        highest_value_palindrome += s[n - i - 1]
                    k -= 1
                min_changes_required -= 1
            # If characters are the same, make one of them '9' if it's not already.
            elif s[i] != '9':
                highest_value_palindrome += '9'
                k -= 2
            else:
                highest_value_palindrome += s[i]
        # If there is only one change opportunity.
        elif k - min_changes_required == 1:
            if s[i] != s[n - i - 1]:
                if s[i] != '9' and s[n - i - 1] != '9':
                    highest_value_palindrome += '9'
                    k -= 2
                else:
                    # Choose the maximum value character to maximize the overall value.
                    if s[i] > s[n - i - 1]:
                        highest_value_palindrome += s[i]
                    else:
                        highest_value_palindrome += s[n - i - 1]
                    k -= 1
                min_changes_required -= 1
            else:
                highest_value_palindrome += s[i]
        # If the remaining opportunities are only enough to make the characters same, choose the maximum.
        elif s[i] != s[n - i - 1]:
            if s[i] > s[n - i - 1]:
                highest_value_palindrome += s[i]
            else:
                highest_value_palindrome += s[n - i - 1]
            k -= 1
            min_changes_required -= 1
        else:
            highest_value_palindrome += s[i]

    # Handle the middle character for odd-length strings.
    if n & 1:
        if k > 0:
            return highest_value_palindrome + '9' + highest_value_palindrome[::-1]

        return highest_value_palindrome + s[n // 2] + highest_value_palindrome[::-1]

    # For even-length strings, simply mirror the part obtained so far.
    return highest_value_palindrome + highest_value_palindrome[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highest_value_palindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
