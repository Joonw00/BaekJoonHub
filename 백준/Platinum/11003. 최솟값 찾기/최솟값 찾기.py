import sys
from collections import deque
N,L = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))
m = deque()

for i in range(N):
  if i-L>=0:
    if m[0] == A[i-L]:
      m.popleft()
  while m:
    if m[-1] <= A[i]:
      break
    m.pop()
  m.append(A[i])
  print(m[0],end=" ")