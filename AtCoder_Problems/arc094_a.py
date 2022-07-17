#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc093/tasks/arc094_a
# testcase
# XX

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true

import io
import sys

_INPUT = """\
2
3 1 2
6 1 1
"""

def canReaach(From, To):
    dt = To[0] - From[0]
    dx = To[1] - From[1]
    dy = To[2] - From[2]
    
    if abs(dx) + abs(dy) <= dt:
        if (dx + dy) % 2 == dt % 2:
            return True
    return False

def main():
    

if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()