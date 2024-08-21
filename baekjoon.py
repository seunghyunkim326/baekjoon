# 커트라인 : N명 응시, 점수 가장 높은 k명 수상 => 수상 커트라인 점수 출력
N, k = map(int,input().split())
score = [int(x) for x in map(int,input().split())]
# 내림차순 정렬 함수 or 알고리즘 사용
for i in range(N):
    for j in range(i+1,N):
        if score[j] > score[i]:
            temp = score[j]
            score[j] = score[i]
            score[i] = temp
print(score[k-1])