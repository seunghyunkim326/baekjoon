# 수 정렬하기 2 : N과 N개의 정수 입력 => 오름차순으로 출력
import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
arr = set()
for _ in range(N):
    temp = int(input())
    arr.add(temp)
result = sorted(arr)
for i in result:
    output(str(i) + "\n")
# GPT가 알려준 방법처럼 for a in b 를 사용하여 집합도 간편하게 한 원소 씩 출력 가능하다.(집합의 정렬로 sort로 가능하다.)