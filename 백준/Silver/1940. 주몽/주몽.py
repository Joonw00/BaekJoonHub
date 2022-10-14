import sys
n = input()
n = int(n)
m = input()
m = int(m)
A = list(map(int, sys.stdin.readline().split()))
A.sort()
f = 0
l = n-1
ans = 0
while f < l:
    s = A[f]+A[l]
    if s == m:
        ans+=1
        f+=1
        l-=1
    elif s < m:
        f+=1
    else:
        l-=1
print(ans)