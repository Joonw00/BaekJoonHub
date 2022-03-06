import sys
import heapq as hq
N = input()
N = int(N)
ar = []


for _ in range(N):
    X = sys.stdin.readline()
    X = int(X)
    if X != 0:      #자연수일 때 추가
        hq.heappush(ar, (-X,X))     #-X기준 최소힙 : X기준 최대힙
    if X == 0:
        if len(ar) == 0:    #0인데, 비었을 때
            print(0)
        else:               #0일 때 출력
            print(hq.heappop(ar)[1])
