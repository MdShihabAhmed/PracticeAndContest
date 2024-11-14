def f(n):
    if n%2:
        return 3*n+1
    return n//2

s = int(input())
if s==1 or s==2:
    print(4)
    exit(0)
a = [s]

temp = f(a[-1])
while(temp!=1):
    a.append(temp)
    temp = f(a[-1])

print(len(a)+2)
