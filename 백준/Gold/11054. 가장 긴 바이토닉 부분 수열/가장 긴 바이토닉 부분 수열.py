import sys
N = input()
N = int(N)
A = list(map(int, sys.stdin.readline().split()))
inc = [1]*N
dec = [1]*N
for i in range(N):  #증가 함수
    for j in range(i):
        if A[i] > A[j] and inc[i] < inc[j]+1:
            inc[i] = inc[j] + 1

for i in range(N-1, -1, -1):    #감소함수
    i = int(i)
    for j in range(N-1, i, -1):   #범위 확인
        j = int(j)
        if A[i] > A[j] and dec[i] < dec[j]+1:
            dec[i] = dec[j] + 1
total = [1]*N
for i in range(N):
    total[i] += inc[i]-1
    total[i] += dec[i]-1
print(max(total))