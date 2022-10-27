from collections import deque
def solution(people, limit):
    s = deque(sorted(people))
    count = 0
    while s:
        if len(s) == 1:
            count +=1
            break
        if s[0] + s[-1] <= limit:
            s.popleft()
            s.pop()
        else:
            s.pop()
        count += 1
    return count

"""
a = 0
b = len(people)-1
while a < b:
    if people[b] + people[a] <= limit:
        a += 1
        answer +=1
    b -= 1
return len(people) - answer
"""

    
