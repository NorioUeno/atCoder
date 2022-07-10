#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc086/tasks/arc089_a
# testcase
# https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAqrgrN537yaSYBi08bzhwpa/AGC013/A?dl=0&subfolder_nav_tracking=1

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
    N = int(input())
    T =[]
    for n in range(N):
        T.append(list(map(int, input().split())))
    
    initial = [0, 0, 0]
    T.insert(0, initial)
    isReadable = True
    for n in range(N + 1):
        if n + 1  <=  N:
            if canReaach(T[n], T[n+1]):
                continue
            else:
                isReadable = False
                break
            

    if isReadable:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()