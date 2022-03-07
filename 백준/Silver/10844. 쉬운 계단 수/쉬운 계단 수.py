import sys
sys.setrecursionlimit(10**5)
N = input()
N = int(N)
#이거 대칭아님? 1,2,3,4랑 9,8,7,6이랑 같은 횟수 같음->dp쓰면 순차적으로 올라가서 응용 못할 듯?

ctn = 0
num = [0]*10*N        #해당 숫자가 몇 번 불리는 지
for i in range(10):
    num[i] = 1
num[0] = 0
#이차원 배열로 [자릿수,숫자]로 초기화, dp개념 응용
for i in range(1,N):
    num[10*i] = num[10*i - 9]       #헷갈려서 for안쓰고 걍 다 적음
    num[10*i + 1] = num[10*i -8] + num[10*i - 10]
    num[10*i + 2] = num[10*i -7] + num[10*i - 9]
    num[10*i + 3] = num[10*i -6] + num[10*i - 8]
    num[10*i + 4] = num[10*i -5] + num[10*i - 7]
    num[10*i + 5] = num[10*i -4] + num[10*i - 6]
    num[10*i + 6] = num[10*i -3] + num[10*i - 5]
    num[10*i + 7] = num[10*i -2] + num[10*i - 4]
    num[10*i + 8] = num[10*i -1] + num[10*i - 3]
    num[10*i + 9] = num[10*i - 2]

sum = 0
for i in range(10):
    sum+=num[10*(N-1)+i]
print(sum%1000000000)
