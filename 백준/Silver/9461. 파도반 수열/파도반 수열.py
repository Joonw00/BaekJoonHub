import sys
T = input()
T = int(T)

dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(1,96):
    i = int(i)
    dp[i+5] = dp[i] + dp[i+4]




for _ in range(T):
    N = input()
    N = int(N)
    print(dp[N])