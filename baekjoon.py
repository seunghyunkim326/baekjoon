# 대표값2 : 5개의 수 입력 => 평균값, 중앙값 출력
arr = []
avg = 0
for _ in range(5):
    A = int(input())
    arr.append(A)
    avg += A
print(int(avg/5))
# 순서가 없고 중복도 가능하네 => 오름차순 정리만 해주자!
for i in range(5):
    for j in range(i,5):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr[2])