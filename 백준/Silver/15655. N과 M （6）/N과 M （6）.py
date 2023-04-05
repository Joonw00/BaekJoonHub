from itertools import combinations, permutations
import sys
n,m=map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
perm = list(combinations(A,m))
for i in range(len(perm)):
    print(*perm[i])