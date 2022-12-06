import sys
    
input = sys.stdin.readline
    
k, n = map(int,input().split())
a = list(map(int,input().split()))
b = set(map(int,input().split()))
    
cumSum = [a[0]]
for i in range(1,k):
    cumSum.append(cumSum[i-1]+a[i])
    
second = set()
flag = True
for i in b:
    temp2 = set()
    for j in range(k):
        temp2.add((i-cumSum[j]))
        
    if flag:
        second = temp2
        flag = False
    second = second.intersection(temp2)
    
print(len(second))