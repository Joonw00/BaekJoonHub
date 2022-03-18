R,C = map(int,input().split())
brd = []
for _ in range(R):
    brd.append(list(input()))
ans = 0
dp = set()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def sch(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    for k in range(4):
        x1 = x+dx[k]
        y1 = y+dy[k]
        if 0 <= y1 < R and 0 <= x1 < C and not brd[y1][x1] in dp:
            dp.add(brd[y1][x1])
            sch(x1,y1,cnt+1)
            dp.remove(brd[y1][x1])
dp.add(brd[0][0])
sch(0,0,1)
print(ans)