#!/opt/homebrew/bin/python3

# import sys

# S = sys.argv


def switch_array(num):
    temp = 0
    if len(array)  -1  == num:
        temp = array[num]
        array[num] = array[num - 1]
        array[num - 1] = temp
    else:
        temp = array[num]
        array[num] = array[num + 1]
        array[num + 1] = temp


N, Q = map(int, input().split())

array = [i for i in range(1, N + 1)]
print(array)

for i in range(Q):
    print(array)
    num = array.index(int(input()))
    switch_array(num)

print(array)