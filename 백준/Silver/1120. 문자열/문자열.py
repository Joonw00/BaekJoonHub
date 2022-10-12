import sys
a,b = map(str, sys.stdin.readline().split())
ans = []
for i in range(len(b) -len(a)+1):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            temp += 1
    ans.append(temp)

print(min(ans))