import os
import sys
import random
import bisect

def get_palindrome_length(s, ll, flag):
    # Use flag = 0 for an odd number of letters in a palindrome, 1 for even
    maxlen = 1
    l1 = ll - 2
    l2 = ll + 1 + flag
    while l1 >= 0 and l2 < len(s) and s[l1] == s[l2]:
        maxlen += 1
        l1 -= 1
        l2 += 1
    return 2 * maxlen + flag

def find_max_palindrome_length(s):
    # Find the length of the longest palindrome in s
    ls = len(s)
    maxlen = 1 
    for ll in range(1, ls):
        if s[ll-1] == s[ll]:
            newlen = get_palindrome_length(s, ll, 0)
            if newlen > maxlen:
                maxlen = newlen
    for ll in range(1, ls-1):
        if s[ll-1] == s[ll+1]:
            newlen = get_palindrome_length(s, ll, 1)
            if newlen > maxlen:
                maxlen = newlen
    return maxlen

def get_palindrome_length_round_fast(slist, ll, lens):
    ls = len(slist)
    if ls == 1:
        return (slist[0][1], slist[0][2])
    start = slist[ll][1]
    end = slist[ll][2]
    l1 = ll - 1
    l2 = ll + 1
    notdone = True
    while notdone and (end - start) < lens and slist[l1 % ls][0] == slist[l2 % ls][0]:
        lgth1 = slist[l1][2] - slist[l1][1]
        if lgth1 < 0:
            lgth1 += lens
        ls2 = l2 % ls
        lgth2 = slist[ls2][2] - slist[ls2][1]
        if lgth2 < 0:
            lgth2 += lens
        lmax = lens - (end - start)
        if lgth1 != lgth2:
            notdone = False
        if lgth1 < lgth2:
            lgth2 = lgth1
        if lgth2 + lgth2 > lmax:
            lgth2 = lmax // 2
            notdone = False
        end += lgth2
        start -= lgth2
        l1 -= 1
        l2 += 1
    return (start, end)

def compress_string(s):
    # Replace strings of contiguous identical characters with (char, #) pairs
    # where # is the end of the string sequence
    ls = []
    cc = '.'
    start = 0
    for ss in range(len(s)):    
        if s[ss] != cc:
            ls.append((cc, start, ss))
            start = ss
            cc = s[ss]
    ls.append((cc, start, len(s)))
    ls.pop(0)
    if ls[0][0] == ls[-1][0]:
        ls[0] = (ls[0][0], ls[-1][1] - len(s), ls[0][2])
        ls.pop()
    return ls

def make_palindrome_dict(slist, lens):
    ls = len(slist)
    dict1 = {}
    list1 = []
    for ll in range(ls):
        (start, stop) = get_palindrome_length_round_fast(slist, ll, lens)
        lgth = stop - start
        if lgth > 1:
            if start < 0:
                start, stop = start + lens, stop + lens
            if lgth in dict1:
                dict1[lgth].append((start, stop))
            else:
                dict1[lgth] = [(start, stop)]
                bisect.insort(list1, lgth)
    for (_, start, stop) in slist:
        lgth = stop - start
        if lgth > 1:
            if start < 0:
                start, stop = start + lens, stop + lens
            if lgth in dict1:
                if (start, stop) in dict1[lgth]:
                    dict1[lgth].remove((start, stop))
                dict1[lgth].append((-start, -stop))
            else:
                dict1[lgth] = [(-start, -stop)]
                bisect.insort(list1, lgth)        
    return (dict1, list1)

def circular_palindromes(s):
    ls = len(s)
    slist = compress_string(s)
    (dict1, list1) = make_palindrome_dict(slist, ls)
    maxes = []
    ll = len(list1) - 1
    for k in range(ls):
        maxlgth = 1 
        done = False
        ks = k + ls
        for ind in range(ll, -1, -1):
            if done:
                break
            lgth = list1[ind]
            if lgth < maxlgth:
                break
            for (start, stop) in dict1[lgth]:
                if start <= 0 and stop <= 0:
                    if -start <= k < -stop:
                        lgth1 = max(-stop - k, k + start) 
                    else:
                        lgth1 = lgth
                    if -start < ks <= -stop:
                        lgth2 = max(ks + start, -stop - ks)
                    else:
                        lgth2 = lgth
                else:
                    if start <= k <= stop:
                        lgth1 = abs(start + stop - k - k)
                    else:
                        lgth1 = lgth
                    if start <= ks <= stop:
                        lgth2 = abs(start + stop - ks - ks)
                    else:
                        lgth2 = lgth
                if lgth1 > lgth2:
                    lgth1 = lgth2
                if maxlgth < lgth1:
                    maxlgth = lgth1
                if lgth1 == lgth:
                    done = True
                    break
        maxes.append(maxlgth)
    return maxes

def rotate_string(s, val):
    val = val % len(s)
    return s[val:] + s[:val]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    result = circular_palindromes(s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
