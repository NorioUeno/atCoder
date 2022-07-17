#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/agc010/tasks/agc010_a
# testcase
# XX

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true

import io
import sys

_INPUT = """\
5
1 2 3 4 5
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd_count = 0
    
    for a in A:
        if a % 2 == 1:
            odd_count += 1
    
    if odd_count % 2 == 0:
        print('YES')
    else:
        print('NO')
    
    
if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()