import sys
    
input = sys.stdin.readline
    
def solver(n, a, x):
    a.sort()
    summ = 0
    result = 0
    for i in range(n):
        summ+=a[i]
        if summ<=x:
            result+=1
            result+=(x-summ)//(i+1)
        else:
            break
    return result
    
for _ in range(int(input())):
    n, x= map(int,input().split())
    a = list(map(int,input().split()))
    
    print(solver(n, a, x))