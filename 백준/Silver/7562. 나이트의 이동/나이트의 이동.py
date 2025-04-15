import sys
from collections import deque


dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(knight, target):
    q = deque()
    q.append(knight)
    visited[knight[0]][knight[1]] = 1

    while q:
        x,y = q.popleft()
        if target[0] == x and target[1] == y:
            return visited[x][y] - 1

        for i in range(8):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if next_x <0 or next_x>=l:
                continue
            if next_y<0 or next_y >=l:
                continue
            if visited[next_x][next_y] != 0:
                continue
            q.append([next_x,next_y])

            # 거리 계산을 위해 숫자 넣기기
            visited[next_x][next_y] = visited[x][y] + 1
    return -1

t = int(input())
for i in range(t):
    l = int(input())
    knight = list(map(int,sys.stdin.readline().split()))
    target = list(map(int,sys.stdin.readline().split()))
    board = [[0]*l for _ in range(l)]
    visited = [[0]*l for _ in range(l)]


    print(bfs(knight,target))


