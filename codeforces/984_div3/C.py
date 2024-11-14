import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    track = [0]*(n+1)
    for i in range(n-3):
        temp = s[i:min(i+4,n)]
        if ['1','1','0','0'] == temp:
            track[i]=1

    total = sum(track)
    q = int(input())
    for i in range(q):
        index, v = input().split()
        index = int(index)-1
        if s[index]!=v:
            for j in range(index,max(0,index-3)-1,-1):
                if track[j]:
                    track[j]=0
                    total-=1
                    break
            s[index] = v
            for j in range(index,max(0,index-3)-1,-1):
                temp = s[j:min(j+4,n)]
                if ['1','1','0','0'] == temp:
                    track[j]=1
                    total+=1
                    break
        if total:
            print("YES")
        else:
            print("NO")
