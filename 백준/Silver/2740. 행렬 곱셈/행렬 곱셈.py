import sys
n1,m1 = map(int,sys.stdin.readline().split())
A = []
B = []
for i in range(n1):
    A.append(list(map(int,sys.stdin.readline().split())))
n2,m2 = map(int,sys.stdin.readline().split())
for i in range(n2):
    B.append(list(map(int,sys.stdin.readline().split())))
for i in range(n1):
    for j in range(m2):
        print(sum([A[i][k]*B[k][j] for k in range(m1)]),end=' ')
    print()
