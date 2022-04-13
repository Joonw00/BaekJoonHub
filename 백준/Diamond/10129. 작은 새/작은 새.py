import sys
from collections import deque
n = input()
n = int(n)
tr = list(map(int, sys.stdin.readline().split()))
q = input()
q = int(q)
#입력
for i in range(q):
  #새의 크기
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
    #불리한 경우에 대한 조건 설정
    while dp[-1][0] >= tired:
      if dp[-1][0] == tired and dp[-1][1]>=h:
        break
      dp.pop()
    #데이터 추가
    dp.append([tired,h,i])
    #sliced
    if i>= dp[0][2]+k:
      dp.popleft()
  print(dp[-1][0])