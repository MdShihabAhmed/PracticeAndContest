import sys
from collections import defaultdict
input = sys.stdin.readline

def check(num,di):
    temp = num
    temp -= min((temp//6),(di["6"]))*6
    temp -= min((temp//2),(di["2"]))*2
    if temp==0:
        return True
    return False




for _ in range(int(input())):
    s = input().strip()
    possible = defaultdict(int)
    su = 0
    for c in s:
        su+=int(c)
        if c=="2":
            possible[c]+=1
        if c=="3":
            possible["6"]+=1
    
    if su%9==0:
        print("YES")
    else:

        temp = 9-(su%9)
        total = possible["6"]*6+possible["2"]*2
        flag = False
        for i in range(10**5+5):
            temp2 = i*9
            if temp2+temp>total:
                break
            # print(temp2,temp,possible)
            if check(temp2+temp,possible):
                flag = True 
                break
        if flag:
            print("YES")    
        else:
            print("NO")
        
        

    
