#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/agc020/tasks/agc020_a
# testcase
# XX

# nums = list(map(int, input().split()))
# N, A, B = map(int, input().split())
# from sqlalchemy import false, true

import io
import sys

_INPUT = """\
5 2 4
"""

def main():
    N, A, B = map(int, input().split())
    diff = B - A
    if diff % 2 == 0:
        print('Alice')
    else:
        print('Borys')
    
if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()