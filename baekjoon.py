# 알고리즘 수업 - 점근적 표기 1 : f(n) = a1n + a0, 양의 정수 c, n0 입력 => 만족 = 1, 불만족 = 0 출력
# O(n)의 정의 : 모든 n>=n0 에 대해 f(n)<=c*g(n)인 양의 상수 c와 n0가 존재
a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
n = n0
while True:
    if a1 * n + a0 > c * n:
        print(0)
        break
    elif n == 101:
        print(1)
        break
    else:
        n += 1