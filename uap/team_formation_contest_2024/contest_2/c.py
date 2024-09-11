h = 0
v = 0
for _ in range(int(input())):
    x, y = input().split()
    if x=='h':
        h+=1
    else:
        v+=1
print(h*v)