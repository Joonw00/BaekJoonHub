import heapq
import sys
n = input()
n = int(n)
heap = []
for i in range(n):
  x = sys.stdin.readline().rstrip()
  x = int(x)
  if x!=0:
    heapq.heappush(heap,[abs(x),x])
  elif x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap)[1])