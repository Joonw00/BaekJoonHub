# 풀이 과정

처음에는 날먹 할 생각으로 small코드에서 ,B,C만 고쳐서 해봄 (안 될 거 알면서 왜 그랬을까)

일단 틀렸습니다가 아닌 시간 초과가 났음

문제 조건 살펴보니 10**4->10**6 으로 바꿔놔서while문으로 돌리면 시간초과 날 수 밖에 없음

딱히 while문이 필요한 과정도 아니라 간단하게A-temp로 조건 별로 처리

2번째 트라이에서 틀렸습니다가 뜸

small과 다른 점이 뭔가 생각하다가 B,C가 설정됐다는 거 밖에 없음을 인지. 처음에는 B,C == 1일 때 문제가 생기나? 싶었음(small에서는 2였으니까)

일단 그 때도 문제는 맞았고, 좀 더 확장 해서 생각 해 보니

i i+1 i+2

B  C   C

i i+1 i+2

B  B   B

이런 개념으로 연산 우선순위가 정해 짐.

다시말 해 B<C라면 B로 다 계산하는 방법이 더 싸다는 뜻임.

B ==C 는 상관 없으니 B<=C와 else로 조건을 분류 해 코드를 다시 작성했음 -> 성공!

# 리뷰

small에서 찜찜했던 느낌을 지울 수 있었음.
