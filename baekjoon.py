# 회사에 있는 사람 : 회사에 있는 모든 사람을 구하는 프로그램
# 출입 기록의 수 N(2<=N<10^6), 각 사람의 이름과 enter 나 leave 입력받음 => 현재 회사에 있는 사람의 이름을 사전의 역순으로 한 줄씩
import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input())
company = []
for _ in range(N):
    name, state = map(str,input().split())
    if state == "enter":
        company.append(name)
    elif state == "leave":
        company.remove(name)
company.sort(reverse=True)
for i in range(len(company)):
    output(company[i] + "\n")
# 시간초과 발생 => sys를 이용해보자!