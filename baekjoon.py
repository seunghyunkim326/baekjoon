# 알고리즘 수행 시간6
def MenOfPassion(A,n):
    sum = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                sum = sum + A[i] * A[j] * A[k]
    return sum

# (n-2)
N = int(input())
print(int((N*(N-1)*(N-2))/6))
print(3)