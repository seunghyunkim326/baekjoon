# 문자열 집합 : N, M 입력, 집합 S에 포함된 N개의 문자열, 검사해야할 M개의 문자열 입력 => M개의 문자열 중 집합 S에 포함된 문자열 갯수 출력
N, M = map(int,input().split())
S = set()
check = []
count = 0
for _ in range(N):
    temp_S = str(input())
    S.add(temp_S)
for _ in range(M):
    temp_check = str(input())
    check.append(temp_check)
for i in range(M):
    if check[i] in S:
        count += 1
    else:
        pass
print(count)