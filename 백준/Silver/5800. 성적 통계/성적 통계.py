import sys
t = int(sys.stdin.readline())
for j in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    gap = 0
    for i in range(1, len(score)):
        score[i-1] = score[i]
    score.pop()
    score.sort()
    for i in range(1,len(score)):
        temp = score[i] - score[i-1]
        if temp > gap:
            gap = temp
    print("Class", j+1)
    print("Max", str(score[-1])+',' ,"Min", str(score[0])+',' , "Largest gap", str(gap))