T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    pointOnLine = N*4 + 1
    cnt = pointOnLine
    for x in range(N-1, 0, -1):
        cnt += 4 * int(((N**2) - (x**2))**0.5)
    print(f'#{test_case} {cnt}')