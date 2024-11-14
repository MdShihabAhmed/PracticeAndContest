import sys

input = sys.stdin.readline
vowels = ['a','e','i','o','u']
for _ in range(int(input())):
    n = int(input())
    s = n//5
    ss = n%5
    result = []
    for i in range(5):
        temp = s
        if ss:
            temp+=1
            ss-=1
        result.append(vowels[i]*temp)

    
    print("".join(result))

        
