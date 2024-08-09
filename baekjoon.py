# 수 정렬하기 : N개의 수 입력 => 이를 오름차순으로 출력(중복X)
# 첫째 줄에 수의 개수 N입력. 둘째 줄부터 N개의 줄에 수가 주어짐.
N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)
# 오름차순으로 정렬하는 코드
for i in range(N):
    for j in range(i,N):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
# 중복없는 오름차순 리스트를 만드는 코드(중복이 아닐 경우에 넣는 코드)
result = []
for k in range(N):
    if arr[k] not in result:
        result.append(arr[k])
for r in range(len(result)):
    print(result[r])