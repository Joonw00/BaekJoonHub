import sys
N = input()
N = int(N)
seq = list(map(int,sys.stdin.readline().split()))

dp = []
dp.append(-1000000001)
for i in range(N):
  if seq[i] > dp[-1]:
    dp.append(seq[i])
  else:
    f = 0
    l = len(dp)
    while f<l:
      mid = (f+l)//2
      #이분 탐색
      if dp[mid] < seq[i]:
        f = mid+1
      else:
        l = mid
    dp[l] = seq[i]
print(len(dp) - 1)
