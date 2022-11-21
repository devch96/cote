Xa, Ya, Xb, Yb, Xc, Yc = map(int,input().split())
answer = 0.0
#기울기 비교(나눗셈은 런타임 에러 가능))
if ((Xa-Xb)*(Ya-Yc)==(Ya-Yb)*(Xa-Xc)):
    print(-1.0)
    exit(0)
def hypot(x, y):
    return ((x**2) + (y**2))**0.5
a = hypot(Xa-Xb, Ya-Yb)
b = hypot(Xb-Xc, Yb-Yc)
c = hypot(Xc-Xa, Yc-Ya)
answer = ((max(a+b, b+c, c+a) - min(a+b,b+c,c+a))*2)
print(answer)