import math
import sys
n,a = map(int,sys.stdin.readline().split())
s = (-1*a)%n     #합
def eea(a,b):
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    K = b
    while b:
        q = a//b
        r = a%b
        a = b
        b = r
        temp = s0
        s0 = s1
        s1 = temp - s1*q
        temp = t0
        t0 = t1
        t1 = temp - t1*q
    if a!=1:
        return 10**9 + 1
    s0 = (s0 % K + K) % K
    return s0
#서로소 아니면 -1반환
if math.gcd(a,n) != 1:
    print(s,-1)
else:
    #계산
    print(s,eea(a,n))
