import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
#선수 정보
order = [0 for _ in range(N+1)]
rev_check = [[] for _ in range(N+1)]
for i in range(M):
  a,b = map(int,sys.stdin.readline().split())
  order[b]+=1
  rev_check[a].append(b)

q = deque()
for i in range(1,N+1):
  i = int(i)
  if order[i] == 0:
    q.append(i)
ans = []
while q:
  temp = q.popleft()
  ans.append(temp)
  for i in rev_check[temp]:
    order[i]-=1
    if order[i] == 0:
      q.append(i)

visited = [False]*(N+1)
for i in ans:
  visited[i] = True
  print(i,end=" ")
for i in range(1,N+1):
  if visited[i] == False:
    print(i,end=" ")