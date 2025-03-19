import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    check = set()
    for num in b:
        check.add(str(num))
    
    firstHalf = sum(b[:n])
    secondHalf = sum(b[n:])
    if str(secondHalf-firstHalf) not in check:
        result = [secondHalf-firstHalf]
        for i in range(n):
            result.append(b[i+n])
            result.append(b[i])
        print(*result)
        continue
    
    first = -1
    flag = False
    for i in range(n):
        x = 2*b[i]-firstHalf+secondHalf
        if x>0 and str(x) not in check:
            first = b[i]
            b[i] = x
            break
    if first<0:
        for i in range(n,2*n):
            x = 2*b[i]+firstHalf-secondHalf
            if x>0 and str(x) not in check:
                first = b[i]
                b[i] = x
                flag = True
                break
    
    if flag:
        result = [first]
        for i in range(n):
            result.append(b[i+n])
            result.append(b[i])
    else:
        result = [first]
        for i in range(n):
            result.append(b[i])
            result.append(b[i+n])
    print(*result)