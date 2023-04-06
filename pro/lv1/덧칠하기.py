def solution(n,m,section):
    answer = 0
    idx = section[0]-1
    for i in section:
        if idx < i:
            idx = i+m-1
            answer += 1
    return answer
        

print(solution(8,4,[2,3,6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))