import sys
a = input()
a = int(a)
A = map(int,sys.stdin.readline().split())
A = list(A)
ans = 0
for i in A:
    if a == i:
        ans+=1
print(ans)