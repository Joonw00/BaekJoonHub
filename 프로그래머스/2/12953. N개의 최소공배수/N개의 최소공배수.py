def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])
    return answer

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i