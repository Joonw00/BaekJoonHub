import copy
import sys
n = input()
n = int(n)
an = [0] * 101
bn = [0] * 101
for _ in range(n):
  x,y = map(int,sys.stdin.readline().split())
  an[x]+=1
  bn[y]+=1
  anum = copy.deepcopy(an)
  bnum = copy.deepcopy(bn)
  #탐색
  a = 1
  b = 100
  ans = 0
  while True:
    if anum[a] == 0:
      a+=1
      if a>100:
        break
      continue
    if bnum[b] == 0:
      b-=1
      if b<0:
        break
      continue
    ans = max(ans,a+b)
    temp = min(anum[a],bnum[b])
    anum[a]-=temp
    bnum[b]-=temp
  print(ans)
    