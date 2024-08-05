# 시간복잡도 알고리즘 수행 시간2 : 수행 횟수, 다음 줄에 수행 횟수를 다항식으로 표현 시, 최고차항의 차수 출력
def MenOfPassion(A,n):
    sum = 0
    for i in range(1,n):
        sum = sum + A[i]
    return sum
# n만큼 실행됨 => A배열의 길이가 n보다 크거나 같다는 가정하에 => O(n)의 시간복잡도를 가짐

n = int(input())
print(n)
print(1)