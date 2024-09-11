n = int(input())
s1 = input().rstrip()
if n==1:
    print(len(s1))
else:
    s2 = input().rstrip()
    i = 0
    result = 0
    while(i<len(s1)):
        l = 0
        temp = 0
        k = i
        while k<len(s1) and l<len(s2) and s1[k]==s2[l]:
            k+=1
            l+=1
            temp+=1
        result = max(result, temp)
        i+=1
    
    i = 0
    result2 = 0
    while(i<len(s2)):
        l = 0
        temp = 0
        k = i
        while k<len(s2) and l<len(s1) and s2[k]==s1[l]:
            k+=1
            l+=1
            temp+=1
        result2 = max(result2, temp)
        i+=1
    
    print((len(s1)+len(s2))-(max(result,result2)))