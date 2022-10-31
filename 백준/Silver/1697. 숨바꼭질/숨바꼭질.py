import sys
n,k = map(int,sys.stdin.readline().split())
def bfs():
    q = [n]
    while q:
        x = q.pop(0)
        if x == k:
            print(visit[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<=100000 and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                q.append(nx)

visit = [0]*100001
bfs()