import sys

input = sys.stdin.readline

n = int(input())
shows = []
for i in range(n):
    l, r = map(int,input().split())
    shows.append([l,r])

shows.sort()
flag = True
first = shows[0][1]
second = 0
if n>1:
    second = shows[1][1]

for i in range(2,n):
    if shows[i][0]>first:
        first = shows[i][1]
        continue
    if shows[i][0]>second:
        second = shows[i][1]
        continue
    flag = False
    break

if flag:
    print("YES")
else:
    print("NO")