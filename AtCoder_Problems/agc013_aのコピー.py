#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/agc013/tasks/agc013_a
# in
# https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAy9caEelKPtPqRXXwx8FsPa/AGC013/A/in?dl=0&subfolder_nav_tracking=1

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true


N = int(input())
A = list(map(int, input().split()))
count = 1
flag = 0
for i in range(N-1):
    if flag == 0:
        if A[i] < A[i+1]:
            flag = 1
        elif A[i] > A[i+1]:
            flag = 2
    elif flag == 1:
        if A[i] > A[i+1]:
            count += 1
            flag = 0
    elif flag == 2:
        if A[i] < A[i+1]:
            count += 1
            flag = 0
print(count)