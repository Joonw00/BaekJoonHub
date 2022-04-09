import sys
from collections import deque
N,L = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))
d = deque()

for i in range(N):
  if i-L>=0:
    if d[0] == A[i-L]:
      d.popleft()
  while d:
    if d[-1] <= A[i]:
      break
    d.pop()
  d.append(A[i])
  print(d[0],end=" ")
