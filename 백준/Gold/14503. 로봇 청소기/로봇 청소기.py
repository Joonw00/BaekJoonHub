import sys
n,m = map(int,sys.stdin.readline().split())

r,c,d = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


ans = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = -1
        ans +=1

    # 사방에 빈칸이 없음음
    if graph[r][c-1] != 0 and graph[r][c+1] != 0 and graph[r-1][c] != 0 and graph[r+1][c] != 0:
        # 후진 되면 후진진
        if d == 0 and graph[r+1][c] !=1:
            r+=1
            continue
        if d == 1 and graph[r][c-1] !=1:
            c-=1
            continue
        if d == 2 and graph[r-1][c] !=1:
            r-=1
            continue
        if d == 3 and graph[r][c+1] !=1:
            c+=1
            continue
    
        #후진 못하면 break
        if d == 0 and graph[r+1][c] ==1:
            break
        if d == 1 and graph[r][c-1] ==1:
            break
        if d == 2 and graph[r-1][c] ==1:
            break
        if d == 3 and graph[r][c+1] ==1:
            break
    #청소되지 않은 칸이 있으면 회전
    d = d-1
    if d < 0 :
        d = 3
        
    if d == 0 and graph[r-1][c] ==0:
        r-=1
        continue
    if d == 1 and graph[r][c+1] ==0:
        c+=1
        continue
    if d == 2 and graph[r+1][c] ==0:
        r+=1
        continue
    if d == 3 and graph[r][c-1] ==0:
        c-=1
        continue
print(ans)