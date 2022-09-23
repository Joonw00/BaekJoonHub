import sys
n,m = map(int,sys.stdin.readline().split())


crb = [list(map(int, input())) for _ in range(n)]
cra = [list(map(int, input())) for _ in range(n)]
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if crb[i][j] != cra[i][j]:
            for k in range(3):
                crb[i+k][j] = (crb[i+k][j] +1)%2
                crb[i+k][j+1] = (crb[i+k][j+1] +1)%2
                crb[i+k][j+2] = (crb[i+k][j+2] +1)%2
            cnt += 1

if crb == cra:
    print(cnt)
else:
    print(-1)