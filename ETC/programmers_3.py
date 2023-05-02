# Programmers Lv.2 최솟값 만들기
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    for i, j in zip(A, B):
        answer += i * j

    return answer