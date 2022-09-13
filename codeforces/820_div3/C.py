import sys
    
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()

    arr = []

    for i in range(len(s)):
        arr.append(ord(s[i])-96)

    f = min(arr[0],arr[-1])
    l = max(arr[0],arr[-1])

    cost = l-f
    result = []
    for i in range(1,len(s)-1):
        if arr[i]>=f and arr[i]<=l:
            result.append([arr[i],i+1])
    if arr[0]<arr[-1]:
        result.sort()
    else:
        result.sort(reverse=True)
    result = [i[1] for i in result]
    result.append(len(s))


    print(cost, len(result)+1)
    print(1,' ', sep='',end='')
    print(*result)