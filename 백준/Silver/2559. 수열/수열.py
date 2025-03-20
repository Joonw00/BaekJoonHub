import sys
n,k = map(int,sys.stdin.readline().split())

A = list(map(int,sys.stdin.readline().split()))

sum = 0
for i in range(k):
    sum+=A[i]

ans = sum
for i in range(k,n):
    sum+=A[i]-A[i-k]
    ans = max(ans,sum)
print(ans)