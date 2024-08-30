# 나는야 포켓몬 마스터 이다솜 : 도감에 수록된 포켓몬 개수 N, 맞춰야 하는 문제 M(1<=M<=100000)개
# N개의 포켓몬 입력, M개의 문제(포켓몬 이름 or 도감에서의 번호)
# M개의 문제에 대한 답을 출력 => 이름이면 도감 번호, 도감 번호면 이름
import sys
input = sys.stdin.readline
output = sys.stdout.write
N, M = map(int, input().split())
arr = []
for i in range(N):
    name = input()
    arr.append(name)
for _ in range(M):
    problem = input()
    try:
        problem = int(problem)
    except:
        problem = str(problem)
    if type(problem) == int:
        output(arr[problem] + "\n")
    elif type(problem) == str:
        num = arr.index(problem) + 1
        output(str(num) + "\n")
# 숫자를 입력해도 문자로 입력받기 때문에 type error 발생 => ASCII 코드를 이용해서 숫자 부분을 추출할까? => 숫자인지만 판별하려면 isdigit() or try 구문 사용하자!
# 시간초과 발생! => 역시 리스트를 사용해서 시간초과가 발생한 걸까? => 번호를 알아야 하니 key 값을 숫자로 하여 풀어볼까?(dictonary)