"""
Z-algorihm
z[i] = (s[:] とs[i:] の共通接頭辞の長さ)
"""
def Z_algorithm(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    i = 1
    j = 0
    while i < n:
        while i+j < n and s[j] == s[i+j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < n and k+z[k] < j:
            z[i+k] = z[k]
            k += 1
        i += k
        j -= k
    return z

############################################
# https://judge.yosupo.jp/submission/24036
#############################################

# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

s = input()
z = Z_algorithm(s)
print(*z)
