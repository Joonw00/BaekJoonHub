import sys

n = int(input())
body = []
for i in range(n):
    body.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(n):
        if body[i][j] == "*":
            hearty = i+1
            heartx = j
            break
    if body[i][j] == "*":
        break

# 팔 길이 구하기
leftArm = -1
for i in range(n):
    if body[hearty][i] == "*" and leftArm == -1:
        leftArm = i
    if (body[hearty][i] != "*" and leftArm != -1):
        rightArm = i
        break
    if i == n-1:
        rightArm = i + 1
leftAns = heartx - leftArm
rightAns = rightArm - heartx -1

# 허리 길이
for i in range(hearty, n):
    if body[i][heartx] == "_":
        bodyEnd = i -1
        bodyAns = bodyEnd-hearty
        break


# 다리 길이
leftLeg = 0
rightLeg = 0
for i in range(bodyEnd+1,n):
    if body[i][heartx-1] != "*":
        leftLeg = i-bodyEnd - 1
        break
    if i == n-1:
        leftLeg = i-bodyEnd
        break

for i in range(bodyEnd+1,n):
    if body[i][heartx+1] != "*":
        rightLeg = i-bodyEnd - 1
        break
    if i == n-1:
        rightLeg = i-bodyEnd
        break

print(hearty+1, heartx+1)
print(leftAns, rightAns, bodyAns, leftLeg, rightLeg)