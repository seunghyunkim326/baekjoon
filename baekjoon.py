# 알고리즘 수행 시간4
def MenOfPassion(A,n):
    sum = 0
    for i in range(1,n):
        for j in range(i+1,n+1):
            sum = sum + A[i] * A[j]
    return sum
N = int(input())
print(int((N/2)*(N-1)))
print(2)