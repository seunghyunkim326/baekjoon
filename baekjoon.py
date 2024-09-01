# 수 정렬하기3 : N, N개의 수 N+1줄에 걸쳐 입력 => N개의 줄에 오름차순 출력(중복O)
# 중복 가능하기 때문에 집합은 불가능 => 리스트로 한 번 해보자
arr = []
N = int(input())
for _ in range(N):
    temp = int(input())
    arr.append(temp)
result = sorted(arr)
for i in range(N):
    print(result[i])