import sys
N,B,C = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cost = 0
if B>C:
  for i in range(N):
    if i+2< N and A[i+1]>A[i+2]:
      temp = min(A[i], A[i+1]-A[i+2])
      A[i]-=temp
      A[i+1]-=temp
      cost+=temp*(B+C)
    if A[i] == 0:
      continue
    if i+2<N:
      temp = min(A[i+2], A[i+1],A[i])
      A[i]-=temp
      A[i+1]-=temp
      A[i+2]-=temp
      cost+=temp*(B+2*C)
    if i == N-2:
      temp = min(A[i],A[i+1])
      A[i]-=temp
      A[i+1]-=temp
      cost+=temp*(B+C)
    cost+=A[i] * B
else:
  for i in range(N):
    cost+= A[i]*B
print(cost)