import sys
N =  input()
N = int(N)
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
S = 0
for i in A:
    M = -1
    for j in B:
        #M에 최대값 저장
        if M < j:
            M = j
    S+=M*i
    B.remove(M)
print(S)