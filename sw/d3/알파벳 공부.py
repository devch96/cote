T = int(input())
for test_case in range(1,T+1):
    string = input()
    cnt = 0
    start = 97
    for s in string:
        if ord(s) == start:
            cnt += 1
            start += 1
        else:
            break
    print(f'#{test_case} {cnt}')
    