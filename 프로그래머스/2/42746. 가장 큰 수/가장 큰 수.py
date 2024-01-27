def solution(numbers):
    answer = ''
    num = list(map(str, numbers)) 
    num.sort(key = lambda x : x*3)
    num.reverse()
    for i in num:
        answer+=i
    if answer[0] == "0":
        answer = '0'
    return answer