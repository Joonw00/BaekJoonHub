import sys
from collections import deque

#M : 가로,N : 세로
M,N = map(int,sys.stdin.readline().split())

#박스의 상태
box = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    box.append(a)
#총 안 익은 개수
tot = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            tot+=1


#익은 토마토의 위치
tom = deque()
cnt = 0
for i in range(N):
    for j in  range(M):
        if box[i][j] == 1:
            #x가 먼저 들어감
            tom.append([j,i])
dx = [1,0,0,-1]
dy = [0,1,-1,0]
while tom:
    cnt+=1
    l = len(tom)
    for _ in range(l):
        a = tom[0][0]
        b = tom[0][1]
        del tom[0]
        for k in range(4):
            x = a+dx[k]
            y = b+dy[k]
            if x>=0 and x<M and y>=0 and y<N and box[y][x] == 0:
                box[y][x] = 1
                tom.append([x,y])
                tot-=1

if tot == 0:
    print(cnt-1)
else:
    print(-1)