import sys
n = int(sys.stdin.readline())
ans = []
ans.append(1)
ans.append(2)
for i in range(2, n):
    ans.append((ans[i-1] + ans[i-2] )% 15746)
print(ans[n-1] % 15746)