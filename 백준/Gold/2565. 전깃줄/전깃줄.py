import sys
N = input()
N = int(N)
seq = []
line = []
for i in range(N):
  a,b = map(int,sys.stdin.readline().split())
  line.append([a,b])
line.sort()
for i in range(N):
  seq.append(line[i][1])

dp = []
dp.append(0)
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
print(N-len(dp)+1)

