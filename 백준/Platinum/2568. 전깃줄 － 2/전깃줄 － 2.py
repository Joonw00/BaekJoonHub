import sys
N = input()
N = int(N)

line = []
for i in range(N):
  a,b = map(int,sys.stdin.readline().split())
  line.append([a,b])
line.sort()

dp = []
dp.append(0)
idx = [0]*500002

for i in range(N):
  if line[i][1] > dp[-1]:
    dp.append(line[i][1])
    idx[line[i][0]] = len(dp) - 1
  else:
    f = 0
    l = len(dp)-1
    while f<l:
      mid = (f+l)//2
      #이분 탐색
      if dp[mid] < line[i][1]:
        f = mid+1
      else:
        l = mid
    dp[l] = line[i][1]
    idx[line[i][0]] = l
print(N - len(dp) + 1)
j = len(dp) - 1

ans = []

for i in range(500000,-1,-1):
  if idx[i] == j:
    idx[i] = 0
    j-=1
  if j == 0:
    break
for i in range(1,500002):
  i = int(i)
  if idx[i] != 0:
    print(i)