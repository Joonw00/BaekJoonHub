import sys
M = 1000000009
n = int(sys.stdin.readline())
dp = [[0 for _ in range(3)] for _ in range(100005)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][2] = 1

for i in range(100001):
    dp[i+1][0] = (dp[i+1][0] + dp[i][1] + dp[i][2]) % M
    dp[i+2][1] = (dp[i+2][1] + dp[i][0] + dp[i][2]) % M
    dp[i+3][2] = (dp[i+3][2] + dp[i][0] + dp[i][1]) % M
for i in range(n):
    t = int(sys.stdin.readline())
    print(sum(dp[t]) % M)