import sys

input = sys.stdin.readline

def solver(n):
    arr = [i for i in range(n,0,-1)]
    print(*arr)
    # if n==3:
    #     for i in range(2,0,-1):    
    #         arr[i],arr[i-1]=arr[i-1],arr[i]
    #         print(*arr)
    #     return

    for i in range(n-1,0,-1):
        arr[i],arr[i-1]=arr[i-1],arr[i]
        print(*arr)
        

for _ in range(int(input())):
    n = int(input())

    solver(n)