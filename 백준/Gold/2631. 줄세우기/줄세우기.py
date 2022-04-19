import sys
N = input()
N = int(N)
child = []
for i in range(N):
  a = sys.stdin.readline().rstrip()
  a = int(a)
  child.append(a)

dp = [1]*N
for i in range(N):
  for j in range(i):
    if child[j] < child[i] and dp[i] < dp[j]+1:
      dp[i] = dp[j]+1
m = max(dp)
print(N-m)