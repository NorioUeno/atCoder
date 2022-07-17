#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc073/tasks/abc073_c
# testcase
# XX

# nums = list(map(int, input().split()))
# N, A, B = map(int, input().split())
# from sqlalchemy import false, true

import io
import sys

_INPUT = """\
6
12
22
16
22
18
12
"""

def main():
    N = int(input())
    list = []
    for n in range(N):
        list.append(int(input()))
    list.sort()
    count_num = 1
    previous_num = 0
    count = 0
    for n in list:
        if previous_num == 0:
            previous_num = n
        elif previous_num == n:
            count_num += 1
        elif count_num % 2 == 1:
            count += 1
            count_num = 0
            previous_num = 0
        else:
            count_num = 1
            previous_num = n
            
    print(count)
    
if __name__ == '__main__':
    sys.stdin = io.StringIO(_INPUT)
    main()