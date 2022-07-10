#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc086/tasks/abc081_b

# nums = list(map(int, input().split()))
# from sqlalchemy import false, true


N = int(input())
nums = list(map(int, input().split()))
count = 0
isEven = True
while isEven:
    for i in range(N):
        if nums[i] % 2 == 0:
            nums[i] = nums[i]/2
        else:
            isEven = False
            break
    if isEven:
        count += 1

print(count)