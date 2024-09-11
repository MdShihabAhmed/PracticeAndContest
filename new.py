def solution(xs):
    # Your code here
    result = 1
    negative = 0
    maxNegative = -1001
    flag = True
    for panel in xs:
        if panel:
            flag = False
            result*=panel
        if panel<0:
            maxNegative = max(maxNegative, panel)
            negative+=1
    if negative%2:
        result//=maxNegative
    
    if flag:
        result = 0
        
    return result

print(solution(list(map(int,input().split()))))