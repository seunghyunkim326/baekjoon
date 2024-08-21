# 수 정렬하기 2 : N 입력, N줄에 걸쳐 수 입력(중복X) => N개의 줄에 오름차순으로 정렬된 수 출력
N = int(input())
arr = []
for _ in range(N):
    temp = int(input())
    arr.append(temp)
for j in range(N):
    for k in range(j+1,N):
        if arr[k] < arr[j]:
            num = arr[k]
            arr[k] = arr[j]
            arr[j] = num
for i in range(N):
    print(arr[i])
# sort를 이용하여 빠르게 해결
# 하지만 시간초과 발생 => 찾는게 빠른 set을 사용할까? => 숫자 뽑는거에 사용하는건 안돼, 그럼 언제 쓰노?
# sort가 오래 걸리는 것인가? => 그럼 이중 for문을 이용해서 해볼까? => 어차피 반복문으로 정렬해도 리스트 슬라이싱 사용하는데?
# 오름차순 정렬 방법에서 시간을 줄여야될거같다. => brute force, sort는 안됨 => 