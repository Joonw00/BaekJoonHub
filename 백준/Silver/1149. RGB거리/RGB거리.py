import sys
N = input()
N = int(N)
cost = []
for i in range(N):
    r,g,b = map(int, sys.stdin.readline().split())
    cost.append([r,g,b])

#dp
cr=[0]*N
cg=[0]*N
cb=[0]*N
cr[0] = cost[0][0]
cg[0] = cost[0][1]
cb[0] = cost[0][2]

for i in range(1,N):
    i = int(i)
    if cg[i-1] < cb[i-1]:
        cr[i] = cost[i][0] + cg[i-1]
    else:
        cr[i] = cost[i][0] + cb[i-1]

    if cr[i-1] < cb[i-1]:
        cg[i] = cost[i][1] + cr[i-1]
    else:
        cg[i] = cost[i][1] + cb[i-1]

    if cr[i-1] < cg[i-1]:
        cb[i] = cost[i][2] + cr[i-1]
    else:
        cb[i] = cost[i][2] + cg[i-1]

ans = min(cb[N-1],cg[N-1],cr[N-1])
print(ans)
    