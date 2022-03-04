import sys
stack = []

N = input()
N = int(N)

for i in range(0,N):
    order= sys.stdin.readline().rstrip()
    leng = len(stack)
    if order[0:4] == "push":
        push_num = order[5:]
        push_num = int(push_num)
        stack.append(push_num)
    elif order == "pop":
        if leng == 0:
            print(-1)
            continue
        else:
            print(stack[leng-1])
            del stack[leng-1]
    elif order == "size":
        print(leng)
    elif order == "empty":
        if leng == 0:
            print("1")
        else:
            print("0")
    elif order == "top":
        if leng ==0:
            print(-1)
            continue
        print(stack[leng-1])