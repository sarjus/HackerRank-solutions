import os
from itertools import zip_longest, islice


def suffix_array(s):
    """
    Computes the suffix array of string s.
    Time Complexity: O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys(s)
    while max(line) < n - 1:
        line = to_int_keys(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line


def inverse_array(arr):
    """
    Computes the inverse array of the given array arr.
    """
    n = len(arr)
    ans = [0] * n
    for i in range(n):
        ans[arr[i]] = i
    return ans


def to_int_keys(arr):
    """
    Converts elements of the array to integer keys.
    """
    seen = set()
    int_keys = []
    for elem in arr:
        if elem not in seen:
            int_keys.append(elem)
            seen.add(elem)
    int_keys.sort()
    index = {v: i for i, v in enumerate(int_keys)}
    return [index[v] for v in arr]


def suffix_matrix(s):
    """
    Computes the suffix matrix of string s.
    """
    n = len(s)
    k = 1
    line = to_int_keys(s)
    ans = [line]
    while max(line) < n - 1:
        line = to_int_keys(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None), fillvalue=-1)])
        ans.append(line)
        k <<= 1
    return ans


def suffix_array_alternative_naive(s):
    """
    An alternative (naive) method to compute the suffix array.
    """
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

def lcp(suffix_matrix, i, j):
    """
    Computes the Longest Common Prefix of suffixes i and j in the suffix matrix.
    """
    n = len(suffix_matrix[-1])
    if i == j:
        return n - i
    k = 1 << (len(suffix_matrix) - 2)
    ans = 0
    for line in suffix_matrix[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


def max_score_value(a):
    """
    Computes the maximum score value based on the input string a.
    """
    suffix_arr = inverse_array(suffix_array(a))
    matrix = suffix_matrix(a)

    lcp_values = [lcp(matrix, suffix_arr[n], suffix_arr[n+1]) for n in range(len(suffix_arr) - 1)]
    lcp_values.append(0)

    max_score = len(a)
    lcp_values_len = len(lcp_values)

    for i, num in enumerate(suffix_arr):
        if lcp_values[i] <= 1:
            continue

        lcp_i = lcp_values[i]

        cnt = 2
        for ii in range(i+1, lcp_values_len):
            if lcp_values[ii] >= lcp_i:
                cnt += 1
            else:
                break
        for ii in range(i-1, -1, -1):
            if lcp_values[ii] >= lcp_i:
                cnt += 1
            else:
                break

        max_score = max(cnt * lcp_i, max_score)

    return max_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = max_score_value(t)

    fptr.write(str(result) + '\n')

    fptr.close()
