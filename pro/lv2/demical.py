import string
def solution(n,t,m,p):
    temp = string.digits + string.ascii_uppercase
    def convert(num, base):
        result = ''
        while num > 0:
            num ,r = divmod(num,base)
            result += temp[r]
        return result[::-1]
    tmp = ''
    answer = ''
    count = 0
    while len(answer) < t*m:
        if count == 0:
            answer += '0'
        answer += convert(count,n)
        count+=1
    return answer[p-1:t*m:m]
print(solution(2,4,2,1))
print(solution(16,16,2,1))
    


    
