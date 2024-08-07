# 수학은 비대면강의 : ax + by =c, dx + ey = f 연립 방정식의 해를 구하는 문제
a, b, c, d, e, f = map(int,input().split())
for x in range(-999,999):
    for y in range(-999,999):
        if a * x + b * y == c and d * x + e * y == f:
            print(x,end=' ')
            print(y)