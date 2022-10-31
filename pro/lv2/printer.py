from collections import deque
def solution(priorities, location):
    s = deque([[idx, i] for idx, i in enumerate(priorities)])
    count = 0
    while s:
        if s[0][1] != max(priorities):
            s.rotate(-1)
        else:
            count += 1
            idx = s.popleft()[0]
            priorities.remove(max(priorities))
            if idx == location:
                return count


