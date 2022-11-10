from collections import deque
def solution(msg):
    dic = {chr(64+i) : i for i in range(1,27)}
    msg = deque(msg)
    answer = []
    temp = ''
    value = 27
    while msg:
        temp += msg.popleft()
        if msg:
            if temp+msg[0] not in dic:
                dic[temp+msg[0]] = value
                value += 1
                answer.append(dic[temp])
                temp = ''
    answer.append(dic[temp])
    return answer
print(solution('KAKAO'))