# 숫자 카드 : N, N개의 정수, M, M개의 정수 입력 => 가지고 있으면 1, 없으면 0 출력
# 가지고 있는 숫자 카드는 N개, N밑은 숫자들을 가짐 => 확인용 M개의 숫자 카드, M밑은 확인용 숫자들
# N = int(input())
# having = [x for x in map(int,input().split())]
# M = int(input())
# check = [y for y in map(int,input().split())]
# for k in range(M):
#     if check[k] in having:
#         print(1,end=' ')
#     else:
#         print(0,end=' ')
# 시간초과 발생 => 이유가 뭘까? => N, M이 1~500000 사이의 값이라 그런가? => 역시 in 연산자 때문이었다.
# in 연산자를 사용해서 having 리스트 길이만큼 탐색을 해야하므로 시간 복잡도 O(N*M)을 가진다.
# 해싱을 이용한 빠른 검색이 가능한 set을 이용하면 해결될것 같다!!
N = int(input())
having = {x for x in map(int,input().split())}
M = int(input())
check = [y for y in map(int,input().split())]
for k in range(M):
    if check[k] in having:
        print(1,end=' ')
    else:
        print(0,end=' ')
# 이러면 O(M)의 시간복잡도를 가지겠지?