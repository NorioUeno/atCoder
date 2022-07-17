#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc093/submissions/33051336
# testcase
# XX

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true

import io
import sys

_INPUT = """\
2 5 4
"""

def main():
    A = list(map(int, input().split()))
    A3 = max(A) * 3 
    sum_A = sum(A)
    
    if A3 % 2 == sum_A % 2:
        print(max(A))
    else:
        print(max(A) + 1)

if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()