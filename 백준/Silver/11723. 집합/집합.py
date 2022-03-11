import sys
M = input()
M = int(M)
def add(n):
    global s
    if n not in s:
        s.append(n)
    return
def remove(n):
    global s
    if n in s:
        s.remove(n)
    return
def check(n):
    global s
    if n in s:
        print(1)
    else:
        print(0)
    return
def toggle(n):
    global s
    if n in s:
        s.remove(n)
    else:
        s.append(n)
    return
def all():
    global s
    s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return
def empty():
    while s:
        s.pop()
    return


global s
s = []
for i in range(M):
    #all때문에 입력 좀 복잡하게 받아야 함
    temp = list(sys.stdin.readline().split())
    op = temp[0]
    if op != 'all' and op!='empty':
        num =int(temp[1])
    if op == 'add':
        add(num)
    elif op == 'remove':
        remove(num)
    elif op == 'check':
        check(num)
    elif op == 'toggle':
        toggle(num)
    elif op == 'all':
        all()
    elif op == 'empty':
        empty()