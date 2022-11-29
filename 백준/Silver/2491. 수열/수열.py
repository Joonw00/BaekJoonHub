import sys
n = int(input())
num = list(map(int, sys.stdin.readline().split()))
l = 0
ans = []
#증가
for i in range(1,n):
    if(num[i-1] <= num[i]):
        l += 1
    else:
        ans.append(l)
        l = 0
ans.append(l)
l = 0
#감소
for i in range(1,n):
    if(num[i-1] >= num[i]):
        l += 1
    else:
        ans.append(l)
        l = 0
ans.append(l)
print(max(ans)+1)