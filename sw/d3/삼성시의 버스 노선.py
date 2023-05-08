T = int(input())
for test_case in range(1,T+1):
    busStop = []
    answer = []
    N = int(input())
    for _ in range(N):
        busStop.append(list(map(int,input().split())))
    P = int(input())
    for _ in range(P):
        cnt = 0
        C = int(input())
        for stop in busStop:
            if stop[0] <= C <= stop[1]:
                cnt += 1
        answer.append(cnt)
    print(f'#{test_case}', end =' ')
    print(*answer)

