#!/opt/homebrew/bin/python3
# url
# https://atcoder.jp/contests/abc086/tasks/abc085_c

keys_ase = [
    'dreamer',
    'eraser',
    'dream',
    'erase',
]
keys = []
for key in keys_ase:
    key = list(key)
    key.reverse()
    keys.append(''.join(key))
 



N, Y = map(int, input().split())
isTrue = False

for x in range(0, N + 1):
    for y in range(0, N + 1 - x):
        z = N - (x + y)
        sum = (10000 * x) + (5000 * y) + (1000 * z)
        if Y == sum:
            print("%d %d %d",x ,y ,z)
            isTrue = True
            break
    if isTrue:
        break

if isTrue:
    print('%s %s %s' % (x, y, z))
else:
    print('%s %s %s' % ( -1, -1, -1))
