T = int(input())
for test_case in range(1,T+1):
    P = input()
    Q = input()
    if P == Q:
        if len(P) == 10:
            answer = 'Y'
        else:
            answer = 'N'
    elif P in Q:
        if Q[len(P)] == 'a':
            answer = 'N'
        else:
            answer = 'Y'
    elif ord(P[-1])+1 == ord(Q[-1]):
        answer = 'N'
    else:
        answer = 'Y'
    print(f'#{test_case} {answer}')