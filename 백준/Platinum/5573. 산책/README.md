# 풀이 과정

처음에는 반복되는 규칙성을 찾는 문제인 줄 알았다(거의 4시간 뻘짓,그래도 규칙성이 나오긴 했다)

하지만 규칙 계산도 복잡하고, 시간복잡도가 넘칠 거 같아서 풀이 방향을 틀었다.

규칙을 찾는 과정에서 얻은 아이디어를 기반으로 풀이했다.

1행만 존재하는(H==1)인 경우를 가정하고 시뮬레이션을 돌려보며 관찰을 해 보다가

한 지점에 n 번 방문한다면, x+1,y 와 x,y+1 로 진행하는 방법이 각 k,n-k의 형태로 나온다는 점을 알게 됐다.

이 후로는 단순 구현문제로 n-1반복 시의 각 글자의 상태를 저장한 후

n번째 시행을 그냥 진행 시켜 나오는 점을 출력한다.

+ n-1반복 후 n번째를 그냥 진행시킨다는 개념을 생각하는 데 꽤 오래 걸렸다.
