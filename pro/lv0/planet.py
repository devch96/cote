def solution(age):
    standard = "abcdefghij"
    answer = ''
    for i in str(age):
        answer += standard[int(i)]
    return answer

"""
return ''.join([chr(int(i)+97) for i in str(age)]
"""
