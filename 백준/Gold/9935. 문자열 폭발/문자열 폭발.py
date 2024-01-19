import sys
word = sys.stdin.readline().strip()
fire = sys.stdin.readline().strip()
lw = len(word)
lf = len(fire)
stack = []
for i in range(lw):
    stack.append(word[i])
    while True:
        if fire == ''.join(stack[-lf:]): # join으로 list를 string으로 바꿔줌
            for i in range(lf):
                stack.pop()
        else:
            break
if stack:
    print(''.join(stack))
else:
    print('FRULA')