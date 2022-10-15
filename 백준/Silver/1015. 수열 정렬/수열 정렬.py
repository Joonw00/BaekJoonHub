import sys
n = input()
n = int(n)
A = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    ans = 0
    for j in range(0,i):
        j = int(j)
        if A[j] <= A[i]:
            ans+=1
    for j in range(i,n):
        j = int(j)
        if A[j] < A[i]:
            ans+=1
    print(ans, end=' ')