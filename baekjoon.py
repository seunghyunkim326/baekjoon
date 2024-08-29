# 수 정렬하기 2 : N 입력, N줄에 걸쳐 수 입력(중복X) => N개의 줄에 오름차순으로 정렬된 수 출력
import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
arr = []
arr2 = []
for _ in range(N):
    arr.append(input())
for i in range(N):
    arr2.append(min(arr))
    arr.remove(min(arr))
# for i in range(N):
#     for j in range(i+1,N):
#         if arr[i] > arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
for k in range(N):
    output(arr2[k])
# sort를 이용하여 빠르게 해결
# 하지만 시간초과 발생 => 찾는게 빠른 set을 사용할까? => 숫자 뽑는거에 사용하는건 안돼, 그럼 언제 쓰노?
# sort가 오래 걸리는 것인가? => 그럼 이중 for문을 이용해서 해볼까? => 어차피 반복문으로 정렬해도 리스트 슬라이싱 사용하는데?
# 리스트를 셋으로 바꿀 시, 오름차순이 적용된 상태로 나오지 않는다 => 셋 자체가 순서가 없기 때문에 그런거 같다.
# 질문 게시판 참고 => 입출력 방식이 느리면 *여러 줄* 입력 or 출력 시, 시간초과가 날 수 있다. => python 이용할 경우 => input 대신 sys.stdin.readline