#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc049/tasks/arc065_a
# https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAuupbRP102bv7GxGETc5pNa/ARC065/C/in?dl=0&subfolder_nav_tracking=1

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true
import re
import sys

def biz_logic(str):
    print("きた")
    global isMatch
    if len(str) == 0:
        isMatch = True
        return isMatch
    if re.search('r$',str):
        if re.search('dreamer$',str):
            str2 = re.sub('^dreamer$','' ,str)
            # if len(str) == 0:
            #     isMatch = True
            #     return isMatch
            biz_logic(str2)
        if re.search('eraser$',str):
            str = re.sub('eraser$','' ,str)
            # if len(str) == 0:
            #     isMatch = True
            #     return isMatch
            biz_logic(str)
    elif re.search('m$',str):
        if re.search('dream$',str):
            str2 = re.sub('dream$','',str)
            biz_logic(str2)
    elif re.search('e$',str):
        if re.search('erase$',str):
            str2 = re.sub('erase$','',str)
            biz_logic(str2)

# S = input()
args = sys.argv
S = args[0]

isMatch = False
biz_logic(S)
if isMatch:
    print('YES')
else:
    print('NO')
