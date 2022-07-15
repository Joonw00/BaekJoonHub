import sys
a,b = map(int,sys.stdin.readline().split())
c = a//b
d = a-c*b
print(c)
print(d)