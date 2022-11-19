import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = [v for v in arr]
newA = 0
flag = 0
q = int(input())

for i in range(q):
    t = list(map(int, input().split()))
    if t[0]==1:
        newA = t[1]
        flag +=1
    elif t[0]==2:
        if flag:
            if arr[t[1]-1]!=-1*flag:
                temp[t[1]-1] = newA
                arr[t[1]-1]=-1*flag
            temp[t[1]-1]+=t[2]
        else:
            temp[t[1]-1]+=t[2]
            arr[t[1]-1]+=t[2]
    else:
        if flag:
            if arr[t[1]-1]!=-1*flag:
                temp[t[1]-1] = newA
                arr[t[1]-1]=-1*flag
            print(temp[t[1]-1])
        else:
            print(temp[t[1]-1])