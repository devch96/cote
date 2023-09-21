T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    count = 0
    distance = list(map(int,input().split()))
    for i in range(N):
        if 0 <= distance[i]+i < N:
            if distance[i] >= 0:
                if distance[i] + distance[i + distance[i]] == 0:
                    count += 1

    print(f'#{test_case} {count}')