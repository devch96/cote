def solution(s,n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            if ord(i)+n > 90:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        elif i.islower():        
            if ord(i)+n > 122:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
    return answer

print(solution("AB",1))
print(solution("a B z",4))

"""
chr((ord(i)-ord('A')+n)%26+ord('A'))
"""
