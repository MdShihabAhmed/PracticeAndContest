prime = []
required = []
for i in range(2,(10**5+1)):
    for j in prime:
        if i%j==0:
            break
    else:
        prime.append(i)
j = 0
for i in range(1,(10**5+1)):
    if j<len(prime) and prime[j]==i:
        j+=1
    else:
        required.append(i)
print(prime)
print(required)