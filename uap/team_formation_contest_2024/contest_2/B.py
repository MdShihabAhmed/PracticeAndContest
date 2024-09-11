result = 0


n = int(input())
coins = list(map(int,input().split()))

i = 4
while(i>=0):
    re = set()
    j = i+1
    temp = n
    re.add(temp//j)
    temp-=temp//j
    