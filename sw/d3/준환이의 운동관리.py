T = int(input())
for test_case in range(1,T+1):
    L,U,X = map(int,input().split())
    if L <= X <= U:
        answer = 0
    elif X > U :
        answer = -1
    else:
        answer = L - X
    print(f'#{test_case} {answer}')