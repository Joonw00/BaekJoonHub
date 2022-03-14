from collections import deque
import sys

def srch(mp,i,j,visited):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    q = []
    q.append([i,j])
    visited[i][j] = True
    while q:
        i,j = q[0][0], q[0][1]
        del q[0]
        for k in range(0,8):
            k = int(k)
            x = j+dx[k]
            y = i+dy[k]
            if 0<=y and y<h and 0<=x and x <w:
                if mp[y][x] == 1 and visited[y][x] == False:
                    #이거 주소 문제로 에러남!!!!!
                    visited[y][x] = True
                    q.append([y,x]) 
while True:
    w,h = map(int, sys.stdin.readline().split())
    #종료 조건
    if w == 0 and h == 0:
        break
    mp = []
    #지도 입력
    for i in range(h):
        a = list(map(int,sys.stdin.readline().split()))
        mp.append(a)
    #선언할 때 이렇게 해서 주소가 꼬인 듯???
    #visited = [[False]*w]*h
    visited = [[False for i in range(w)] for j in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if mp[i][j] == 1 and visited[i][j] == False:
                count+=1
                srch(mp,i,j,visited)
    print(count)