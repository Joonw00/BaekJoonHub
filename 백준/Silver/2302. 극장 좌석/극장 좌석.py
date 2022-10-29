import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

se = [0] *41
se[0] = 1
se[1] = 1
se[2] = 2
for i in range(3, 41):
    se[i] = se[i-1] + se[i-2]
ml = []
for i in range(m):
    a = sys.stdin.readline().rstrip()
    a = int(a)
    ml.append(a)

if m>0:
    ans = se[ml[0]-1]
    if n != ml[-1]:
        ml.append(n+1)
    for i in range(1, len(ml)):
        ans = ans * se[ml[i] - ml[i-1] - 1]
    print(ans)
else:
    print(se[n])