import sys
    
input = sys.stdin.readline

n, t = map(int,input().split())
a = list(map(int,input().split()))

left = right = 0
result = current = 0
while left<n and right<n:
	
	while right<n and not(current+ a[right]>t):
		current += a[right]
		right+=1
	
	result = max(result, right - left)# right is extra 1 here
	current -= a[left]
	left += 1

print(result)
