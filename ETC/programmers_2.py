# Programmers Lv.2 JadenCase 문자열 만들기
def solution(s):
    answer = ''
    words = list(s.lower().split(" "))
    result = []
    
    for word in words:
        if word != " ":
            try:
                int(word[0])
                result.append(word)
            except:
                result.append(word.title())
        else:
            result.append(word)
    
    answer = " ".join(result)
            
    return answer