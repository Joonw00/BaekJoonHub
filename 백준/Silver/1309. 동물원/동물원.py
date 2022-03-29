import sys
N = input()
N = int(N)

#순서, 존재여부(0:없음)
dp = [1,1,1]

for i in range(1,N):
    i = int(i)
    a = dp[1] + dp[2]
    b = dp[0] + dp[2]
    c = dp[1] + dp[0] + dp[2]
    dp[0] = a
    dp[1] = b
    dp[2] = c
ans = dp[0] + dp[1] + dp[2]
print(ans%9901)