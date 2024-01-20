import sys
x = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
tot = 0
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    tot += a*b
if x == tot:
    print("Yes")
else:
    print("No")