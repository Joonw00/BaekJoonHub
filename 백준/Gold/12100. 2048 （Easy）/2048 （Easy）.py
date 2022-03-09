import copy
import sys
global N
global m
m = 0   #최대치
N = input()
N = int(N)
br = []    #보드
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    br.append(a)
def move(n,brd):    #남은 시행횟수 N, 현재 보드의 상태 brd
    global N
    global m
    if n==0:
        #가장 큰 수 저장
        for i in range(N):
            for j in range(N):
                m = max(m, brd[i][j])
        return

    bd = copy.deepcopy(brd)
    move(n-1, movel(bd))
    
    bd = copy.deepcopy(brd)
    move(n-1, mover(bd))

    bd = copy.deepcopy(brd)
    move(n-1, moveup(bd))
    
    bd = copy.deepcopy(brd)
    move(n-1, movedn(bd))
    return

def movel(brd):        #보드 상태만 표현
    global N
    #일단 0빼기
    for i in range(N):  #모든 세로줄에 대해
        e = 0   #차있는 자리
        for j in range(N):  #각 가로줄에서
            if brd[i][j] != 0:  #첫 0이아닌 수를 0번째로
                brd[i][e] = brd[i][j]
                if e!=j:    #맞나?
                    brd[i][j] = 0
                e+=1
    #수 합치기
    for i in range(N):  
        for j in range(N-1):
            if brd[i][j] == brd[i][j+1]: 
                brd[i][j] = 2*brd[i][j]
                brd[i][j+1] = 0
    for i in range(N):  #다시 0빼기
        e = 0  
        for j in range(N):
            if brd[i][j] != 0:
                brd[i][e] = brd[i][j]
                if e!=j: 
                    brd[i][j] = 0
                e+=1    
    return brd        
def mover(brd):
    global N
    for i in range(N):
        e = N-1  
        for j in range(N-1, -1, -1): 
            if brd[i][j] != 0:  
                brd[i][e] = brd[i][j]
                if e!=j:  
                    brd[i][j] = 0
                e-=1
    for i in range(N):  
        for j in range(N-1, 0, -1):
            if brd[i][j] == brd[i][j-1]: 
                brd[i][j] = 2*brd[i][j]
                brd[i][j-1] = 0
    for i in range(N):  
        e = N-1   
        for j in range(N-1, -1, -1): 
            if brd[i][j] != 0:
                brd[i][e] = brd[i][j]
                if e!=j:
                    brd[i][j] = 0
                e-=1
    return brd    
def moveup(brd):
    global N
    #일단 0빼기
    for j in range(N):  #모든 가로줄에 대해
        e = 0   #차있는 자리
        for i in range(N):  #각 세로줄에서
            if brd[i][j] != 0:  #첫 0이아닌 수를 0번째로
                brd[e][j] = brd[i][j]
                if e!=i:    #맞나?
                    brd[i][j] = 0
                e+=1
    #수 합치기
    for j in range(N):  
        for i in range(N-1):
            if brd[i][j] == brd[i+1][j]: 
                brd[i][j] = 2*brd[i][j]
                brd[i+1][j] = 0
    for j in range(N):  #다시 0빼기
        e = 0  
        for i in range(N):
            if brd[i][j] != 0:
                brd[e][j] = brd[i][j]
                if e!=i: 
                    brd[i][j] = 0
                e+=1  
    return brd    
def movedn(brd):
    global N
    #일단 0빼기
    for j in range(N):  #모든 가로줄에 대해
        e = N-1   #차있는 자리
        for i in range(N-1, -1, -1):  #각 세로줄에서
            if brd[i][j] != 0:  #첫 0이아닌 수를 0번째로
                brd[e][j] = brd[i][j]
                if e!=i:    #맞나?
                    brd[i][j] = 0
                e-=1
    #수 합치기
    for j in range(N):  
        for i in range(N-1,0,-1):
            if brd[i][j] == brd[i-1][j]: 
                brd[i][j] = 2*brd[i][j]
                brd[i-1][j] = 0
    for j in range(N):  #다시 0빼기
        e = N-1 
        for i in range(N-1, -1, -1):
            if brd[i][j] != 0:
                brd[e][j] = brd[i][j]
                if e!=i: 
                    brd[i][j] = 0
                e-=1  
    return brd    
move(5,br)
print(m)
