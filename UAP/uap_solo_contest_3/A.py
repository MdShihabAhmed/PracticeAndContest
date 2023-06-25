import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

if len(first) != len(second):
    print("NO")
else:
    result = []
    for i in range(len(first)):
        if first[i]!=second[i]:
            result.append(i)
    
    if len(result)==2:
        if first[result[0]]==second[result[1]] and first[result[1]]==second[result[0]]:
            print("YES")
        else:
            print("NO")
    elif len(result)==0:
        print("YES")
    else:
        print("NO")