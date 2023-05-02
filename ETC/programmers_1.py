# Programmers Lv.2 최댓값과 최솟값

def solution(s):
    answer = ''
    numbers = list(map(int, s.split()))

    max = numbers[0]
    min = numbers[1]
    for i in range(0, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        elif numbers[i] < min:
            min = numbers[i]

    answer = f"{min} {max}"

            
    return answer