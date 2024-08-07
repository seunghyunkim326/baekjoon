# 알고리즘 수행 시간3
def MenOfPassion(A,n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            sum = sum + A[i] * A[j]
    return sum
N = int(input())
print(N**2)
print(2)