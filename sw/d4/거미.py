import math
def is_collinear(points, tol=1e-9):
    # 3개 미만의 좌표는 한 평면에 있을 수 없음
    if len(points) < 3:
        return False
    
    # 임의의 3개 점을 선택하여 평면 방정식의 계수를 구함
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]
    a = (y2-y1)*(z3-z1) - (z2-z1)*(y3-y1)
    b = (z2-z1)*(x3-x1) - (x2-x1)*(z3-z1)
    c = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    d = -(a*x1 + b*y1 + c*z1)
    
    # 모든 점에 대해 평면 방정식을 만족하는지 확인
    for point in points[3:]:
        x, y, z = point
        if not math.isclose(a*x + b*y + c*z + d, 0, rel_tol=tol):
            return False
    
    return True

T = int(input())
for i in range(1,T+1):
    bugs = int(input())
    bugPoint = []
    for _ in range(bugs):
        bugPoint.append(list(map(int,input().split())))
    if is_collinear(bugPoint):
        print(f'#{i} TAK')
    else:
        print(f'#{i} NIE')    

