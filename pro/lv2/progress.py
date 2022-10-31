from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        stack = []
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            stack.append(progresses.popleft())
            speeds.popleft()
            if len(progresses) == 0:
                break
        if stack:
            answer.append(len(stack))
    return answer
print(solution([93,30,55],[1,30,5]))



