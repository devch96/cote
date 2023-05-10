#회의실 배정
import sys
input = sys.stdin.readline
N = int(input())
timeTable = [list(map(int,input().split())) for _ in range(N)]
timeTable.sort(key=lambda x:x[0])
timeTable.sort(key=lambda x:x[1])
end_time = 0
cnt = 0
for start,end in timeTable:
    if start >= end_time:
        end_time = end
        cnt += 1
print(cnt)