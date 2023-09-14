import sys
n = int(sys.stdin.readline())
end = [[0,0] for i in range(n+2)]
end[1] = [0,1]
end[2] = [1,0]

for i in range(3,n+1):
    end[i][0] = end[i-1][0] + end[i-1][1]
    end[i][1] = end[i-1][0]

print(end[n][0] + end[n][1])