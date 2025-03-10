import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

ans = 0
for i in A:
    i -= B
    ans += 1
    if i>0:
        ans += int(i/C)
        if i%C:
            ans += 1
print(int(ans))