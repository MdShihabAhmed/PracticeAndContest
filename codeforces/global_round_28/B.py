import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    numbers = {str(i) for i in range(1,n+1)}
    result = [0]*(n)
    val = 1
    for i in range(k-1,n,k):
        result[i]=val
        numbers.remove(str(val))
        val+=1

    for i in range(n):
        if result[i]:
            continue
        result[i]=int(numbers.pop())
    
    print(" ".join(map(str,result)))
