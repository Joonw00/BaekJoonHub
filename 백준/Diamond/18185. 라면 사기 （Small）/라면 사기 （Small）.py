import sys
N = input()
N = int(N)
A = list(map(int, sys.stdin.readline().split()))

cost = 0
for i in range(N):
  if i+2< N and A[i+1]>A[i+2]:
    temp = min(A[i], A[i+1]-A[i+2])
    A[i]-=temp
    A[i+1]-=temp
    cost+=temp*5
  while A[i]:
    A[i]-=1
    cost+=3
    if i+1<N and A[i+1] > 0:
      A[i+1]-=1
      cost+=2
      if i+2<N and A[i+2]>0:
        A[i+2]-=1
        cost+=2
print(cost)