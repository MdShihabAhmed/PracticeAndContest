i = 27
print(bin(i))
for j in range(1,101):
    d = i^j
    if d==0:
        continue

    if j%d==0:
        print(i,j," for ",j,": ",d)