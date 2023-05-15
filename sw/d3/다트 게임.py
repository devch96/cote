def distance(x,y):
    return int((x**2 + y**2)**0.5)

TC = int(input())
for test_case in range(1,TC+1):
    N = int(input())
    score = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if (distance(x,y) // 20) > 10:
            continue
        score += 10 - (distance(x,y) // 20)
    print(f'#{test_case} {score}')