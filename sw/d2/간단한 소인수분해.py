T = int(input())
def count(N,s):
    cnt = 0
    while(N/s == N//s):
        N = N//s
        cnt += 1
    return cnt

for test_case in range(1,T+1):
    N = int(input())
    print(f'#{test_case} {count(N,2)} {count(N,3)} {count(N,5)} {count(N,7)} {count(N,11)}')

        