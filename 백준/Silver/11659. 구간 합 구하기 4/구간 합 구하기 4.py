import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
sum = 0
sav = []
sav.append(0)
for i in range(N):
    sum+=A[i]
    sav.append(sum)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())    
    ans = sav[b] - sav[a-1]
    print(ans)