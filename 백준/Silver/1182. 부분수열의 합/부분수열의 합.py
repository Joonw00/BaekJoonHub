import sys
from itertools import combinations
n,s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
ans = 0
for i in range(1,n+1):
    for j in combinations(a,i):
        if sum(j) == s:
            ans += 1
print(ans)
