import sys
N = input()
N = int(N)
seq = list(map(int,sys.stdin.readline().split()))

dp = []
dp.append(-1000000001)
idx = [0]*(N+1)
for i in range(N):
  if seq[i] > dp[-1]:
    dp.append(seq[i])
    idx[i] = len(dp) - 1
  else:
    f = 1
    l = len(dp)
    while f<l:
      mid = (f+l)//2
      #이분 탐색
      if dp[mid] < seq[i]:
        f = mid+1
      else:
        l = mid
    dp[l] = seq[i]
    idx[i] = l
print(len(dp) - 1)
j = len(dp) - 1
ans = []
for i in range(N,-1,-1):
  if idx[i] == j:
    ans.append(seq[i])
    j-=1
  if j == 0:
    break
for i in range(len(dp)-1):
  print(ans[-1-i],end=" ")
