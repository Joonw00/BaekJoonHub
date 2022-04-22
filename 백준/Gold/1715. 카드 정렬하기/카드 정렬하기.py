import sys
import heapq
N = input()
N = int(N)
card = []
for i in range(N):
  a = sys.stdin.readline().rstrip()
  a = int(a)
  heapq.heappush(card, a)

if N == 1:
  print(0)
else:
  ans = 0
  while True:
    a = heapq.heappop(card)
    if card:
      b = heapq.heappop(card)
      heapq.heappush(card,a+b)
      ans += a+b
    else:
      print(ans)
      break