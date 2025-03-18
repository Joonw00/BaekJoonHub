from itertools import combinations
import sys
n = int(input())
ans = float('inf') 
ability = []
for i in range(n):
    ability.append(list(map(int,sys.stdin.readline().split())))


num = [i for i in range(n)]
for A in combinations(num, n//2):
    B = [x for x in num if x not in A]
    tempA = 0
    tempB = 0
    for i in range(n):
        for j in range(n):
            if i in A and j in A:
                tempA += ability[i][j]
            if i in B and j in B:
                tempB += ability[i][j]

    ans = min(ans, abs(tempA - tempB))

print(ans)

