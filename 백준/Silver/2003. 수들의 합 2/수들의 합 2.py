import sys
n,m  =map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
i = 0
j = 0
sum = A[0]
count = 0
while i <= j and j < n:
    if sum < m:
        j += 1
        if j < n:
            sum += A[j]
    elif sum == m:
        count += 1
        j += 1
        if j < n:
            sum += A[j]
    else:
        sum -= A[i]
        i += 1
        if i > j and i < n:
            j = i
            sum = A[i]
print(count)