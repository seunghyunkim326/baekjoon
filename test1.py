def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 시간 복잡도: O(n)
A = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(A,8)
print(result)