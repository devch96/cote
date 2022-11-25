from collections import deque
n = int(input())
lt = deque([i for i in range(1,n+1)])
flag = 1
while len(lt) > 1:
    if flag % 2 != 0:
        lt.popleft()
        flag += 1
    else:
        lt.append(lt.popleft())
        flag += 1
print(lt[0])