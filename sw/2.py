T = int(input())
for test_case in range(1,T+1):
    N, D = map(int,input().split())
    delayLocation = []
    delayTime = []
    start = 0
    startFlag = True
    DFlag = True
    for _ in range(N):
        location, time = map(int,input().split())
        delayLocation.append(location)
        delayTime.append(time)
    while start != D:
        if delayLocation and delayTime:
            if start == delayLocation[0]:
                if delayTime[0] == 0:
                    delayLocation.pop(0)
                    delayTime.pop(0)
                    startFlag = True
                else:
                    startFlag = False
                    delayTime[0] -= 1
        if delayLocation and delayTime:
            if D == delayLocation[-1]:
                if delayTime[-1] == 0:
                    delayLocation.pop()
                    delayTime.pop()
                    DFlag = True
                else:
                    DFlag = False
                    delayTime[-1] -= 1
        if startFlag:
            start += 1
        if DFlag:
            D -= 1
    print(f'#{test_case} {start}')
