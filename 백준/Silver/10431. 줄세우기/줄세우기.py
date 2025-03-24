import sys

p = int(input())


for i in range(p):
    sorted_height = []
    height = list(map(int,sys.stdin.readline().split()))
    sorted_height.append(height[1])
    sum = 0
    for j in range(2,len(height)):
        sorted_height.append(height[j])
        sorted_height.sort()
        for k in range(len(sorted_height)):
            if height[j] == sorted_height[k]:
                idx = k
                break
        sum+= len(sorted_height) - idx - 1

    print(i+1, sum)
