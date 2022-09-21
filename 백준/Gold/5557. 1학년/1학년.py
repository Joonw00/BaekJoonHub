import sys
n = input()
n = int(n)
num = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(21)]  for _ in range(n)]
dp[0][num[0]]+=1
for i in range(n-1):
    i = int(i)
    for j in range(21):
        if dp[i][j]:
            if j+num[i+1] <= 20:
                dp[i+1][j+num[i+1]] += dp[i][j]
            if j-num[i+1] >= 0:
                dp[i+1][j-num[i+1]] += dp[i][j]
print(dp[-2][num[-1]])