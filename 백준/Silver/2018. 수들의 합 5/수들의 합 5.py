import sys
n = int(sys.stdin.readline().strip())
f = 1
l = 2
s = 3
ans = 0
while f <= n:
    if s <n:
        l+=1
        s+=l
    if s == n:
        ans+=1
        s-=f
        f+=1
    if s > n:
        s-=f
        f+=1
if n == 1:
    ans = 1
    
print(ans)