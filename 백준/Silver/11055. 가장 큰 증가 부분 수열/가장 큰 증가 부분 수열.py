import sys
l = input()
l = int(l)
A = list(map(int, sys.stdin.readline().split()))
sum = []
for i in range(l):
    sum.append(A[i])

for i in range(l):
    for j in range(i):
        if A[i]>A[j] and sum[i] < A[i]+sum[j]:  #and이전: 증가하고,
            sum[i]=A[i]+sum[j]

print(max(sum))