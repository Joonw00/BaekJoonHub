import sys
r,c = map(int,sys.stdin.readline().split())
fld = []
for i in range(r):
    fld.append(list(sys.stdin.readline().rstrip()))

visitied = [[0 for _ in range(c)]for _ in range(r)]
totw = 0
tots = 0
for i in range(r):
    for j in range(c):
        if fld[i][j] != "#" and visitied[i][j] == 0:
            visitied[i][j] = 1
            q = [[i,j]]
            wlf = 0
            sh = 0
            if fld[i][j] == "o":
                sh += 1
            elif fld[i][j] == "v":
                wlf += 1
                
            while q:
                x,y = q.pop(0)
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<r and 0<=ny<c and fld[nx][ny] != "#" and visitied[nx][ny] == 0:
                        visitied[nx][ny] = 1
                        if fld[nx][ny] == "v":
                            wlf += 1
                        elif fld[nx][ny] == "o":
                            sh += 1
                        q.append([nx,ny])
            if wlf >= sh:
                totw += wlf
            else:
                tots += sh
print(tots,totw)