import sys
n = int(sys.stdin.readline())
A = []
for i in range(n):
    A.append(int(sys.stdin.readline()))
A.sort()
for i in range(n):
    print(A[-1-i])