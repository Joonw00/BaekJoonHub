import sys
import heapq
N = input()
N = int(N)
day = []
for i in range(N):
  d,w = map(int, sys.stdin.readline().split())
  heapq.heappush(day,[-w,d])

score = [0]*1001
for i in range(N):
  temp = heapq.heappop(day)
  w = -temp[0]
  d = temp[1]
  while d:
    if score[d] !=0:
      d-=1
      continue
    score[d] = w
    break
ans = 0
for i in range(1,1001):
  i = int(i)
  ans+=score[i]
print(ans)