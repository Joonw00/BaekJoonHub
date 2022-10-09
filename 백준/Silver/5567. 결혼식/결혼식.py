import sys
n = input()
n = int(n)
m = input()
m = int(m)
friend = [[0 for _ in range(n+1)] for _ in range(n+1)]
mem = [0] * (n+1)
mem[1] = 1
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    friend[a][b] = 1
    friend[b][a] = 1
for i in range(1,n+1):
    if friend[1][i] == 1:
        mem[i] = 1
        for j in range(1,n+1):
            if friend[i][j] == 1:
                mem[j] = 1

print(sum(mem)-1)