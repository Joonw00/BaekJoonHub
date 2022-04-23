import sys
import heapq
T = input()
T = int(T)
for _ in range(T):
  N = input()
  N = int(N)
  print(N//2 + 1)
  max_heap = []
  min_heap = []
  num = []
  num.clear()
  while N>0:
    num.extend(list(map(int,sys.stdin.readline().split())))
    N-=10
  i = 0
  for a in num:
    i+=1
    #개수 맞추기
    if len(max_heap) == len(min_heap):
      heapq.heappush(max_heap,(-a,a))
    else:
      heapq.heappush(min_heap,(a,a))
    #min힙 비었을 경우 예외 처리
    if i == 1:
      print(a,end=" ")
      continue
    if max_heap[0][1] > min_heap[0][1]:
      temp = heapq.heappop(max_heap)
      temp2 = heapq.heappop(min_heap)
      heapq.heappush(max_heap, (-temp2[1],temp2[1]))
      heapq.heappush(min_heap, (temp[1],temp[1]))
    if i%2 == 1:
      print(max_heap[0][1],end=" ")
  print("")