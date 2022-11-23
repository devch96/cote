N,m,M,T,R = map(int,input().split())
total = 0
n = 0
now = m
while n<N:
    if m+T > M:
        break
    if now+T <= M:
        now += T
        n += 1
    else:
        now = max(now - R, m)
    total+=1
print(total if n == N else -1)