def solution(s):
    zero_count = 0
    change = 0
    while s != "1":
        zero_count += s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s))[2:])
        change+=1
    return [change, zero_count]

print(solution("110010101001"))
