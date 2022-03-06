import sys
sys.setrecursionlimit(10000) 

M,N = map(int, sys.stdin.readline().split())        #M이 세로
line = []   #각 행
for i in range(M):
    line.append(sys.stdin.readline())
fld = []
for i in range(M):          #fld의 각 좌표에, 나올 수 있는 최대 경로 수 입력
    fld.append([0]*N) 
fld[0][0] = 1
X=[]
Y=[]
X.append(0)
Y.append(0)
while True: #조건 바꿀 것
    if len(X) == 0:
        break
    x = X.pop(0)        #인덱스 0부터 반환하므로,방문처리가 된 곳은 이후 방문 시보다 값이 작다.
    y = Y.pop(0)
    if y == M-1 and x == N-1:
        print(fld[y][x])
        break

    if x+1 < N:
        if line[y][x+1] == '1' and fld[y][x+1] == 0:    #fld값이 0이면 방문한적없음
            fld[y][x+1] = fld[y][x]+1 #방문 처리
            X.append(x+1)
            Y.append(y)
    if y+1 < M:
        if line[y+1][x] == '1' and fld[y+1][x] == 0:      
            fld[y+1][x] = fld[y][x]+1
            X.append(x)
            Y.append(y+1)  
    if x-1 >= 0:
        if line[y][x-1] == '1' and fld[y][x-1] == 0: 
            fld[y][x-1] = fld[y][x]+1
            X.append(x-1)
            Y.append(y)           
    if y-1 >= 0:
        if line[y-1][x] == '1' and fld[y-1][x] == 0:
            fld[y-1][x] = fld[y][x]+1
            X.append(x)
            Y.append(y-1)

#DP개념 문제는 재귀보다 for뤂이 더 편한듯?for이 돌아가면서 시행횟수가 따라 와서 그런듯
