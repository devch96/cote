import math
def solution(n,a,b):
    count = 0
    if max(a,b) % 2 == 0 and abs(a-b) == 1:
        return 1
    while True:
        count += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if max(a,b) % 2 == 0 and abs(a-b) == 1:
            count += 1
            break
    return count

"""
return ((a-1)^(b-1)).bit_length()


answer = 0
while a != b:
    answer += 1
    a, b = (a+1)//2, (b+1)//2

return answer
"""
