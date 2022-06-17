import sys

input = sys.stdin.readline

def solver(n,a):
    a.sort()
    redSum=0
    blueSum=a[0]
    left = 0
    right = n
    while(left<right-1):
        right-=1
        left+=1
        redSum+=a[right]
        blueSum+=a[left]
        if redSum>blueSum:
            return "YES"

    return "NO"

    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(n,a))