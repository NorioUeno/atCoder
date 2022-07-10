#!/opt/homebrew/bin/python3
# Pythonのコーディング 標準入力
# 

import re
import sys


def isTriangle(a,b,c):
    calc = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0])(b[1] - a[1])
    if calc != 0:
        return True
    else:
        return False

args = sys.argv
n = int(input())

x,y = [],[]
for i in range(n):
    aa,bb=list(map(int,input().split()))
    x.append(aa)
    y.append(bb)

triangle_count = 0
# a,b,c = [],[],[]
for i in range(n):
    for j in range(i+1):
        for k in range(j+1):
            a = list(x[i],y[i])
            b = list(x[j],y[j])
            c = list(x[k],y[k])
            if isTriangle(a,b,c):
                triangle_count += 1
    
print(triangle_count)


