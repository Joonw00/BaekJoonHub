import sys
n = input()
n = int(n)
w = list(map(int, sys.stdin.readline().split()))
w.sort()
s = 1
for i in w:
    if s<i:
        break
    s += i
print(s)