T=int(input())
for test_case in range(1,T+1):
    x,y = map(int,input().split())
    if x >= 10 or y >= 10:
        print(f'#{test_case} -1')
        continue
    print(f'#{test_case} {x*y}')