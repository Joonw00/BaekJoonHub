import sys
n = input()
n = int(n)
num = list(map(int,sys.stdin.readline().split()))
m = input()
m = int(m)
dp = [[False]*n for _ in range(n)]
for l  in range(n):
  for s in range(n-l):
    e = s+l
    if l == 0:
      dp[s][e] = True
      continue
    if num[s] == num[e]:
      if l == 1:
        dp[s][e] = True
        continue
      if dp[s+1][e-1]:
        dp[s][e] = True
for _ in range(m):
  s,e = map(int,sys.stdin.readline().split())
  if dp[s-1][e-1]:
    print(1)
  else:
    print(0)