import sys
N = input()
N = int(N)
A = list(map(int, sys.stdin.readline().split()))

#현재까지 가장 큰 높이
big = []

big.append([A[0],1])
print(0,end=" ")

for i in range(1,N):
  i = int(i)
  while big[-1][0]< A[i]:
    big.pop()
    if len(big) == 0:
      break
  if len(big) != 0:
    if big[-1][0] == A[i]:
      big.pop()
  big.append([A[i],i+1])
  if len(big) <= 1:
    print(0,end=" ")
    continue

  print(big[-2][1],end=" ")
