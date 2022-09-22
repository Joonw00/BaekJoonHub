import sys
n = input()
n = int(n)
A = list(map(int, sys.stdin.readline().split()))
heig = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == A[i] and heig[j] == 0:
            heig[j] = i + 1
            break
        elif heig[j] == 0:
            cnt += 1
for i in heig:
    print(i, end = ' ')
