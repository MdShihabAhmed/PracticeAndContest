import sys

input = sys.stdin.readline

def solver(a, n):
    newArr = dict()
    for i in range(n):
        if str(a[i]) in newArr:
            newArr[str(a[i])][0] = newArr[str(a[i])][1]
            newArr[str(a[i])][1] = i+1
        else:
            newArr[str(a[i])] = [0, i+1]
    result = 0

    for value in newArr.values():
        result = max(value[0], result)
    
    return result



for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(a, n))