import sys

input = sys.stdin.readline

def solver(greater, less):
    bessiePosition = greater + less
    result = float('inf')
    for i in bessiePosition:
        count = 0
        for j in greater:
            if i<j:
                count+=1
        
        for j in less:
            if i>j:
                count+=1
        result = min(result, count)

    return result

for i in range(1):
    greater = []
    less = []
    for j in range(int(input())):
        loc, p = input().split()
        
        if loc == 'G':
            greater.append(int(p))
        else:
            less.append(int(p))

    print(solver(greater,less))