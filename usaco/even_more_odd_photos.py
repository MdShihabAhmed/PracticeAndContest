import sys

input = sys.stdin.readline

n = int(input())
breedID = list(map(int,input().split()))

odd = even = 0
for i in range(n):
    if breedID[i]%2:
        odd+=1
    else:
        even+=1

result = 0

temp = min(odd, even)
result += temp*2

odd -= temp
even -= temp
if not odd:
    result+=1
else:
    result += (odd//3)*2
    odd%=3
    result+=odd//2
    odd%=2
    result-=odd

print(result)