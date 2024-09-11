n = int(input())

cont=0
for i in range(n-1,0,-1):
    cont+=1
    if n%i==0:
        break
print(cont)