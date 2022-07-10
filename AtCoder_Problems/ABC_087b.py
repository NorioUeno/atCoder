#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc086/tasks/abc087_b

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true

a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for i in range(0, a + 1):
    for j in range(0, b + 1):
        for k in range(0, c + 1):
            calc = (500 * i) + (100 * j) + (50 * k)
            # print(calc)
            if x == calc:
                count += 1

print(count)