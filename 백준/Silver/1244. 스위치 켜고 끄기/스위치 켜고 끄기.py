import sys

switch_count = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))

student_count = int(sys.stdin.readline())

for i in range(student_count):
    s, n = map(int, sys.stdin.readline().split())
    if s == 1:
        for j in range(n, switch_count+1, n):
            switch[j-1] = 1 - switch[j-1]
    else:
        switch[n-1] = 1 - switch[n-1]
        for k in range(1, switch_count+1):
            if n-1-k < 0 or n-1+k >= switch_count:
                break
            if switch[n-1+k] == switch[n-1-k]:
                switch[n-1+k] = 1 - switch[n-1+k]
                switch[n-1-k] = 1 - switch[n-1-k]
            else:
                break


for i in range(switch_count):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()