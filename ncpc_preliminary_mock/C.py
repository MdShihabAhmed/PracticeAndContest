import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    neg = False
    pos = False
    summ = 0
    move = 0
    for i in range(n):
        number = arr[i]
        if number<0:
            neg = True
        else:
            pos = True
            summ+=number
            if neg:
                move+=1
                neg = False
    neg1 = False
    pos1 = False
    summ1 = 0
    move1 = 0
    for i in range(n-1,-1,-1):
        number = arr[i]
        if number<0:
            neg1 = True
        else:
            pos1 = True
            summ1+=number
            if neg1:
                move1+=1
                neg1 = False
    if pos:
        print(f"Case {_+1}: {summ} {min(move,move1)}")
    else:
        print(f"Case {_+1}: {max(arr)} {0}")