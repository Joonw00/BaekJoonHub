import sys
n = int(sys.stdin.readline())
tr = list(map(int, sys.stdin.readline().split()))
d = 0
tr.sort()
for i in range(n):
    d = max(d, tr[-i-1] + i + 2)

print(d)