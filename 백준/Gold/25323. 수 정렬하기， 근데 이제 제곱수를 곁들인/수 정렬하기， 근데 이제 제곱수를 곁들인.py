import bisect
import copy
import math
import sys
n = input()
n = int(n)
A = list(map(int,sys.stdin.readline().split()))
B = copy.deepcopy(A)
B.sort()
ans = 1
for i in range(n):
    g = math.gcd(A[i],B[i])
    a = A[i] // g
    b = B[i] // g
    if  (int(math.sqrt(a)))**2 != a:  #제곱수x라면    
        ans = 0
        break
    if  (int(math.sqrt(b)))**2 != b:  
        ans = 0
        break
if ans == 1:
    print("YES")
else:
    print("NO")