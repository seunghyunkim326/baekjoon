# 브루트 포스 블랙잭 : 카드 개수 N, 고른 카드의 합 M을 입력받음, 다음 줄에 N개의 카드를 입력받음
# 3장의 카드의 합이 M을 넘지 않고 M에 가장 가까운 값(3자의 카드 합) 출력
N, M =map(int,input().split())
arr = [int(x) for x in input().split()]
sum = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            temp = arr[i] + arr[j] + arr[k]
            if temp > M:
                pass
            else:
                if temp > sum:
                    sum = temp
print(sum)
# 