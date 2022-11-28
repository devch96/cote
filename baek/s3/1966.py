from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, idx = map(int,input().split())
    impo = deque(list(map(int,input().split())))
    impo_ = deque([0 for i in range(n)])
    impo_[idx] = 1
    cnt = 0
    while True:
        if impo[0] == max(impo):
            cnt += 1
            if impo_[0] == 1:
                print(cnt)
                break
            else:
                impo.popleft()
                impo_.popleft()
        else:
            impo.rotate(-1)
            impo_.rotate(-1)