import sys
n = int(input())

def findLongestColor(board):
    num = 0
    for i in range(n):
        temp = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                temp+=1
            else:
                temp = 1
            num = max(num, temp)

    for i in range(n):
        temp = 1
        for j in range(1,n):
            if board[j][i] == board[j-1][i]:
                temp+=1
            else:
                temp = 1
            num = max(num, temp)
    
    return num

# 입력 방식 확인
board = [list(input().strip()) for _ in range(n)]

ans = 0
#가로 교체
for i in range(n):
    for j in range(n-1):
        temp = board[i][j]
        board[i][j] = board[i][j+1]
        board[i][j+1] = temp
        ans = max(ans, findLongestColor(board))
        temp = board[i][j]
        board[i][j] = board[i][j+1]
        board[i][j+1] = temp


#세로로 교체
for i in range(n-1):
    for j in range(n):
        temp = board[i][j]
        board[i][j] = board[i+1][j]
        board[i+1][j] = temp
        ans = max(ans, findLongestColor(board))
        temp = board[i][j]
        board[i][j] = board[i+1][j]
        board[i+1][j] = temp

print(ans)