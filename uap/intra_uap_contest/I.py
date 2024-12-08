import sys

input = sys.stdin.readline

s = input().strip()
a, b = s.split(".")
d, b = b.split("e")
first = a+d[:min(len(d),int(b))]+"0"*(max(0,int(b)-len(d)))
second = d[min(len(d),int(b)):]

if second:
    temp = len(second)
    for i in range(len(second)-1,-1,-1):
        if second[i]=="0":
            temp = i
            continue
        break

    second = second[:temp]
if not first:
    first = 0

if second:
    print(f"{first}.{second}")
else:
    print(first)
