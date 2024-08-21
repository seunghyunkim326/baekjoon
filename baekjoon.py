# 수 정렬하기 2 : N 입력, N줄에 걸쳐 수 입력(중복X) => N개의 줄에 오름차순으로 정렬된 수 출력
N = int(input())
arr = []
for _ in range(N):
    temp = int(input())
    arr.append(temp)
arr.sort()
for i in range(N):
    print(arr[i])