import sys
from math import gcd,sqrt

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x = input().rstrip()
    a = [[0,0]]
    result = []
    for i in range(n):
        if x[i]=='D':
            a.append([a[-1][0]+1, a[-1][1]])
        else:
            a.append([a[-1][0], a[-1][1]+1])
        
        g = gcd(a[-1][0],a[-1][1])
        divisors = set()
        for j in range(1,int(sqrt(g))+1):
            if not g%j:
                divisors.add(j)
                divisors.add(g//j)
        divisors = list(divisors)
        divisors.sort(reverse=True)
        flag = False
        for number in divisors:
            num = (i)//number+1
            previousD = a[num][0]-a[0][0]
            previousK = a[num][1]-a[0][1]
            for k in range(num, i+2, num):
                currentD = a[k][0]-a[k-num][0]
                currentK = a[k][1]-a[k-num][1]
                if not (currentD*previousK==previousD*currentK):
                    break
                previousD = currentD
                previousK = currentK
            else:
                flag = True
                result.append(str(number))
            if flag:
                break

    print(" ".join(result))