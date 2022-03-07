#접근 : DP
#이유 : p 와 sub p 결정이 간편,무조건 지나는 지점의 반복 시행

import sys
T = input()
T = int(T)


for _ in range(T):
    sum = [0]*15
    sum[0] = 1
    n = sys.stdin.readline()
    n = int(n)
    for i in range(n):
        sum[i+1] += sum[i]
        sum[i+2] += sum[i]
        sum[i+3] += sum[i]
    print(sum[n])