import sys
h,w,n = map(int,sys.stdin.readline().split())
walk = []
for i in range(h):
  walk.append(list(map(int,sys.stdin.readline().split())))
dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
dp[0][0] = n-1
for i in range(h):
  for j in range(w):
    temp = dp[i][j]
    if dp[i][j] %2 == 0:
      dp[i][j+1] += temp//2
      dp[i+1][j] += temp//2
    else:
      if walk[i][j]%2 == 0:
        dp[i+1][j] += temp//2 + 1
        dp[i][j+1] += temp//2
      else:
        dp[i][j+1] += temp//2 + 1
        dp[i+1][j] += temp//2
ansx = 0
ansy = 0
while True:
  if (dp[ansy][ansx]+walk[ansy][ansx])%2 == 0:
    ansy+=1
  else:
    ansx+=1
  if ansy == h or ansx == w:
    break
print(ansy+1,ansx+1)