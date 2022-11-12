from collections import deque
def solution(k, dungeons):
    process = deque()
    process.append([k,[]])
    answer = 0
    while process:
        cur,passed = process.popleft()
        for i in range(len(dungeons)):
            [least , use] = dungeons[i]
            if i not in passed and cur >= least and cur - use >= 1:
                process.append([cur - use, passed + [i]])
            else:
                answer = max(answer, len(passed))
    return answer
print(solution(80,[[80,20],[50,40],[30,10]]	))