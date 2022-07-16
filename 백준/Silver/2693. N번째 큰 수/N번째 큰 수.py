import sys
t = input()
t = int(t)
for i in range(t):
    A = list(map(int, input().split()))
    A.sort()
    print(A[7])