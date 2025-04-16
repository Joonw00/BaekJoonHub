import sys
from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# h 높이에서 몇 개의 안전 영역이 생기는 지
def countArea(h):
    count = 0
    area = [[0]*n for _ in range(n)]

    def bfs(i,j):
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        q = deque()
        q.append([i,j])
        area[i][j] = 1
        while q:
            x,y= q.popleft()
            # 4방위에 대해
            for k in range(4):
                next_x = x+dx[k]
                next_y = y+dy[k]

                # 이미 방문 했거나, 경계선 넘어가는 경우 continue
                if next_x<0 or next_x>=n:
                    continue
                if next_y<0 or next_y>=n:
                    continue
                if area[next_x][next_y] == 1:
                    continue

                # q에 추가하고, 방문 처리
                q.append([next_x, next_y])
                area[next_x][next_y] = 1

    # 잠긴 지역 체크크
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                area[i][j] = 1
    
    # 전체 순회하면서 bfs
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                bfs(i,j) # 연결된 곳들 area에 방문 처리리
                count+=1





    return count





ans = 0
for h in range(0,101):
    ans = max(ans, countArea(h))
print(ans)