import sys
n = int(input())
m = int(input())

x = list(map(int,sys.stdin.readline().split()))

compare = 0
ans = 0
for i in range(len(x)):
    ans = max(ans, x[i] - compare)
    compare = x[i]
ans = max(ans, x[0]*2, (n-x[-1])*2)
if ans %2 == 0:
    print(ans//2)
else:
    print(ans//2 + 1)