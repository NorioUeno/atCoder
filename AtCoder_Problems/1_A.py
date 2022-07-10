#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc086/tasks/abc086_a


# nums = list(map(int, input().split()))
a, b= (map(int, input().split())

product = a * b

if product % 2 == 0:
    print("Even")
else:
    print("Odd")
    