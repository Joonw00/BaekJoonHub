from math import ceil
import sys
n = input()
n = int(n)
s = input()
A = list(map(int,sys.stdin.readline().split()))
i = 0
comp = []
str = 1 #처음인지 여부
while i < n:
    temp = 0
    col = s[i]
    while col == s[i]:
        if i == n-1:
            temp = 0 #마지막 연속은 계산x
            i+=1
            break
        if i != 0:
            temp = max(temp,A[i])
        i+=1
    if str == 1:
        str = 0
        temp = 0
    if temp != 0:
        comp.append(temp)

comp.sort(reverse=True)
ans = sum(comp[0:ceil(len(comp)/2)])
print(ans)