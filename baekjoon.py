# 숫자 카드 : N, N개의 정수, M, M개의 정수 입력 => 가지고 있으면 1, 없으면 0 출력
# 가지고 있는 숫자 카드는 N개, N밑은 숫자들을 가짐 => 확인용 M개의 숫자 카드, M밑은 확인용 숫자들
N = int(input())
having = [x for x in map(int,input().split())]
M = int(input())
check = [y for y in map(int,input().split())]
for k in range(M):
    if check[k] in having:
        print(1,end=' ')
    else:
        print(0,end=' ')