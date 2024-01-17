import sys
    
input = sys.stdin.readline

def find_divisors(number):
    divisors = set()
    for i in range(1,int(number**0.5)+1):
        if not number%i:
            divisors.add(i)
            divisors.add(number//i)

    divisors = list(divisors)

    return sorted(divisors)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    divisors = find_divisors(sum(a))
    
    flag = False
    result = 0
    for number in divisors:
        temp = 0
        result = 0
        for i in range(n):
            temp+=a[i]
            if number>temp:
                result+=1
                continue
            elif number==temp:
                temp = 0
            else:
                break
        
            if i==n-1:
                flag = True
        if flag:
            break
    print(result)