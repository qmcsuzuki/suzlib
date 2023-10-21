# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1208
from math.rational.RationalBinarySearch import *

import sys
readline = sys.stdin.readline

def main():
    while 1:
        p,n = map(int,readline().split())
        if p==n==0: break
        
        check = lambda a,b: a*a >= b*b*p
        is_valid = lambda a,b: a <= n and b <= n
    
        a,b,c,d = RationalBinarySearch(check,is_valid)
        print(f"{c}/{d} {a}/{b}")

if __name__ == '__main__':
    main()
