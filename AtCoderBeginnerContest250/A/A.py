#!/opt/homebrew/bin/python3

# import sys

# S = sys.argv
# H, W, R, C = map(str, S[1].split())
H, W = map(int, input().split())
R, C = map(int, input().split())

N = 0

for i in range(1, H + 1):
    for j in range(1, W + 1):
        # print(i, j, R, C)
        # print(abs(R - i))
        # print(abs(C - j))
        if abs(R - i) + abs(C - j) == 1:
            N += 1
print(N)
