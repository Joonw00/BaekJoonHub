import heapq
import sys
k,n = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
heap = []
for i in num:
  heapq.heappush(heap,i)

for t in range(n):
  temp = heapq.heappop(heap)
  for i in num:
    heapq.heappush(heap,i*temp)
    if temp%i == 0:
      break
print(temp)