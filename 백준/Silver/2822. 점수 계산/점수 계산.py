import sys
import copy
tot = 0
A = []
for i in range(8):
    a = int(sys.stdin.readline())
    A.append(a)
B = copy.deepcopy(A)
A.sort(reverse=True)
for i in range(5):
    tot += A[i]
print(tot)
ans = []
for i in range(5):
    for j in range(8):
        if A[i] == B[j]:
            ans.append(j+1)
ans.sort()
for i in range(5):
    print(ans[i], end=' ')