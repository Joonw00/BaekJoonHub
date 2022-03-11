import sys
global L
global C
global spell
global ans

L,C = map(int, sys.stdin.readline().split())
spell = []  # 단어들 저장
ans = []

spell = sys.stdin.readline().split()
spell.sort()

def pas():
    global L
    global C
    global spell
    global ans
    if len(ans) == L:   #꽉 찼으면
        count = 0
        for i in range(0,len(ans)):    #자음 개수 확인
            i = int(i)
            if ans[i] == 'a' or ans[i] =='e' or ans[i] =='i' or ans[i] =='o' or ans[i] =='u':
                count+=1
        if count ==0 or count>=len(ans)-1:
            return
        for i in range(0,L):
            i = int(i)
            print(ans[i],end='')
        print("")
        return
    for i in spell:
        
        if len(ans)!=0:
            if ord(ans[len(ans)-1]) > ord(i):  #사전순이 아니라면
                continue
        if i not in ans:
            ans.append(i)
            pas()
            ans.pop()

pas()