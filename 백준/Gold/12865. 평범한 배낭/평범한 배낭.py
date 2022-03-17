import sys
N,K = map(int, sys.stdin.readline().split())


wv = []
wv.append([0,0])
d = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    wv.append([a,b])

for i in range(1,N+1):
    i = int(i)
    for j in range(1,K+1):
        j = int(j)
        w = wv[i][0]
        v = wv[i][1]
        if j<w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w]+v, d[i-1][j])

print(d[N][K])