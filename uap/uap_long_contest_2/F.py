import sys
from collections import defaultdict

input = sys.stdin.readline

def process(s):
    alpha = [0]*(26)
    for c in s:
        t = ord(c)-ord('a')
        alpha[t] = (alpha[t]+1)%2
    
    re = 0
    for i in range(26):
        if alpha[i]:
            re+=(2**i)
    
    return (alpha,re)

n = int(input())
num = []
alphas = []
for i in range(n):
    s = input().strip()
    alpha,re = process(s)
    num.append(re)
    alphas.append(alpha)

d = defaultdict(int)

result = 0
for nu in num:
    result+=d[nu]
    d[nu]+=1

for i in range(n):
    for j in range(26):
        if alphas[i][j]==1:
            result+=d[num[i]-2**j]

print(result)