import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))

result = []
for cube in towers:

    left = 0
    right = len(result)-1
    key = -1
    while(left<=right):
        mid = (left+right)//2
        if result[mid]<=cube:
            left = mid + 1
        else:
            key = mid
            right = mid - 1
    
    if key==-1:
        result.append(cube)
    else:
        result[key]=cube
print(len(result))