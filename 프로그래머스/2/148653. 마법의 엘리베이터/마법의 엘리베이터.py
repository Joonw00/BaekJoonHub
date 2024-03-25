def solution(storey):
    answer = 0
    while storey:
        end = storey %10    #1의 자리
        if end <5:
            answer+=end
        if end > 5:
            answer+=10-end
            storey += 10
        if end == 5:
            temp = (storey //10)%10 #10의자리
            #특이 케이스 : 45,55,65
            #55는 상관 없음  -> 555예외 상황
            if temp<5:
                answer+=end
            if temp>=5:
                answer+=10-end
                storey+=10
        storey = storey// 10
    return answer