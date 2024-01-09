import sys
n = int(sys.stdin.readline())  #색종이 수
board = [[0]*101 for _ in range(101)]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            board[j][k] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            cnt += 1
print(cnt)