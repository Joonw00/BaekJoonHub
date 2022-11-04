import sys
n,k = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
print(A[k-1])