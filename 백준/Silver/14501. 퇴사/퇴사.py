import sys
n = input()
n = int(n)
dp = [0] * 30
T = []
P = []
for i in range(n):
    t,p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)
for i in range(n):
    for j in range(i+T[i], 30):
        dp[j] = max(dp[i]+P[i],dp[j])
print(max(dp[0:n+1]))