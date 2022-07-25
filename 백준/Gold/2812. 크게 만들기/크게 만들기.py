import sys
n,k = map(int,sys.stdin.readline().split())
num = input()
s = []
s.append(int(num[0]))
for i in range(1,n):
    temp = int(num[i])
    while s and (k>0 and temp > s[-1]):
        s.pop()
        k-=1
    s.append(temp)
while k>0:
    s.pop()
    k-=1
for i in s:
    print(i,end='')