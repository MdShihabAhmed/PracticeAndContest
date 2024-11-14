import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b,c,r = map(float,input().split())
    s = (a+b+c)/2
    large = (s*(s-a)*(s-b)*(s-c))**0.5
    small = (large*r)/(1+r)
    result = (a*(small/large)**0.5)
    # print(small,large,r,small/(large-small))
    print(f"Case {_+1}: {result}")