import sys

input = sys.stdin.readline

def ask(i, j, k):
    print("?",i,j,k)
    sys.stdout.flush()
    ans = int(input())
    return ans

def pr(i,j,k):
    print("!",i,j,k)
    sys.stdout.flush()

for _ in range(int(input())):
    n = int(input())
    i = 1
    j = 2
    k = 3
    cnt = 0
    while(cnt<75):
        ans = ask(i,j,k)
        if ans==0:
            pr(i,j,k)
            break
        cnt+=1
        if cnt>=75:
            break
        ans1 = ask(i,ans,k)
        if ans1==0:
            pr(i,ans,k)
            break
        cnt+=1
        if cnt>=75:
            break
        
        ans2 = ask(i,j,ans)
        if ans2==0:
            pr(i,j,ans)
            break
        cnt+=1
        if cnt>=75:
            break

        ans3 = ask(ans,j,k)
        if ans3==0:
            pr(ans,j,k)
            break
        cnt+=1
        if cnt>=75:
            break
        
        i = ans1
        j = ans2 
        k = ans3

