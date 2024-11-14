import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = ''
    i = 0
    while(i<2*n):
        temp = '0'
        print("?",s+temp)
        sys.stdout.flush()
        ans = int(input())
        i+=1
        if ans:
            s+=temp
            if len(s)==n:
                break
            continue
        
        temp = '1'
        print("?",s+temp)
        sys.stdout.flush()
        ans = int(input())
        i+=1
        if ans:
            s+=temp
            if len(s)==n:
                break
            continue
        break
    if len(s)==n:
        print("!",s)
        sys.stdout.flush()
        continue
    
    while(i<2*n):
        temp = '0'
        print("?",temp+s)
        sys.stdout.flush()
        ans = int(input())
        i+=1
        if ans:
            s=temp+s
            if len(s)==n:
                break
            continue
        
        temp = '1'
        s=temp+s
        if len(s)==n:
            break

    print("!",s)
    sys.stdout.flush()