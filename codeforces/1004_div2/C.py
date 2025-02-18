import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if "7" in s:
        print("0")
        continue
    
    n = len(s)
    
    result = float('inf')
    for i in range(1,n+5):
        cnt = 0
        temp = str(9)*i
        num = int(s)
        while(True):
            if "7" in str(num):
                break
            cnt+=1
            num += int(temp)
        result = min(result, cnt)
    
    print(result)
