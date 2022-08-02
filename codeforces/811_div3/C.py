import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = int(input())
    temp = s
    temp2 = 9
    result = []
    while(temp>0):
        if temp-temp2>=0:
            result.append(temp2)
            temp-=temp2
        temp2-=1
    
    print(''.join([str(result[i]) for i in range(len(result)-1,-1,-1)]))
