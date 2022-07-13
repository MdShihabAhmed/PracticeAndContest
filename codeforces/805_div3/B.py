import sys
from math import ceil

input = sys.stdin.readline

def solver(s):
    temp = set()
    counter =0
    for c in s:
        temp.add(c)
        if len(temp)>3:
            counter+=1
            temp.clear()
            temp.add(c)

    if len(temp)>0:
        counter+=1
    
    return counter



for _ in range(int(input())):
    s = input().rstrip()

    print(solver(list(s)))