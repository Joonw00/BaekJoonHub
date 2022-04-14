import sys
from collections import deque
n = input()
n = int(n)
tr = list(map(int, sys.stdin.readline().split()))
q = input()
q = int(q)

for i in range(q):
  #나는 거리
  k = sys.stdin.readline().rstrip()
  k = int(k)
  #[피로도,h,위치]
  dp = deque()
  dp.append([0,tr[0],0])
  for i in range(1,n):
    i = int(i)
    tired = dp[0][0]
    if dp[0][1] <= tr[i]:
      tired+=1
    
    h = tr[i]
    idx = i
    #의미 없는 정보들 pop
    while dp[-1][0] >= tired:
      if dp[-1][0] == tired and dp[-1][1]>=h:
        break
      dp.pop()

    dp.append([tired,h,i])
    #slice
    if i>= dp[0][2]+k:
      dp.popleft()
  print(dp[-1][0])
