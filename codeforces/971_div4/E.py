import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    

    start = k
    end = n+k-1

    result = float("inf")
    while(start<=end):
        mid = (start+end)//2
        first = ((mid-k+1)*(2*k+(mid-k+1)-1))//2
        second = ((n+k-1-mid-1+1)*(2*(mid+1)+(n+k-1-mid-1+1)-1))//2
        result = min(result, abs(first-second))
        # print(result,first,second,mid,start,end,_)
        if first<=second:
            start = mid+1
        elif first>second:
            end = mid-1

    
    print(result)
        


