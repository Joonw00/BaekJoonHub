import sys
import heapq
N = input()
N = int(N)

max_heap = []
min_heap = []
for i in range(N):
  a = sys.stdin.readline().rstrip()
  a = int(a)
  #개수 맞추기
  if len(max_heap) == len(min_heap):
    heapq.heappush(max_heap,(-a,a))
  else:
    heapq.heappush(min_heap,(a,a))
  #min힙 비었을 경우 예외 처리
  if i == 0:
    print(a)
    continue
  if max_heap[0][1] > min_heap[0][1]:
    temp = heapq.heappop(max_heap)
    temp2 = heapq.heappop(min_heap)
    heapq.heappush(max_heap, (-temp2[1],temp2[1]))
    heapq.heappush(min_heap, (temp[1],temp[1]))
  print(max_heap[0][1])