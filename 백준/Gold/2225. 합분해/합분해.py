import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][1] = 1

for k in range(2, K + 1):
    for i in range(N + 1):
        for j in range(i + 1):
            dp[i][k] += dp[j][k - 1]
            dp[i][k] %= 1000000000

print(dp[N][K])
