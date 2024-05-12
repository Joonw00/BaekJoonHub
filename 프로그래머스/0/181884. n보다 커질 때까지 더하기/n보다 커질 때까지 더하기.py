def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer+=i
        if n<answer:
            break
    return answer