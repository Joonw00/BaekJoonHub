import sys
n = input()
n = int(n)
seq = list(map(int,sys.stdin.readline().split()))
dp = [-10000] * (n+1)
dp[0] = seq[0]
for i in range(1,n):
  i = int(i)
  dp[i] = max(dp[i-1]+seq[i], seq[i])
print(max(dp))