import sys
import math
t = int(sys.stdin.readline().strip())

for i in range(t):
    num = list(map(int,sys.stdin.readline().strip().split()))
    ans = 0
    l = len(num)
    for j in range(1,l):
        for k in range(j+1,l):
            ans += math.gcd(num[j],num[k])
    print(ans)