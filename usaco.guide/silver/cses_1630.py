import sys

input = sys.stdin.readline

n = int(input())
tasks = []

for i in range(n):
    a, d = map(int,input().split())
    tasks.append([a,d])

tasks.sort()

f = 0
result = 0
for i in range(n):
    f += tasks[i][0]
    result += (tasks[i][1]-f)
#     print(result)
# print(tasks)
print(result)