import sys
n = int(sys.stdin.readline())
stair = []
for i in range(n):
    a = int(sys.stdin.readline())
    stair.append(a)
dp = [[0,0] for _ in range(n+1)]
#0:이전에 한칸, 1: 이전에 두칸
if n!=1:
    dp[2][0] = stair[1]+stair[0]
for i in range(n+1):
    if i+2 <= n:
        dp[i+2][1] = max(max(dp[i][0],dp[i][1]) +stair[i+1], dp[i+1][1])
    if i+1 <= n:
        dp[i+1][0] = max(dp[i][1] + stair[i], dp[i+1][0])
print(max(dp[-1]))
