import sys
n = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split()))

ans = 0
for i in x:
    for j in x:
        ans += abs(i-j)
print(ans)