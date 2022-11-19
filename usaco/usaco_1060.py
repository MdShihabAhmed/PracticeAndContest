import sys

def solver():
	n = int(input())
	flowers = list(map(int,input().split()))

	result = n
	k = 0
	for i in range(n):
		k+=1
		for j in range(n-k):
			if (sum(flowers[j:j+k+1])/len(flowers[j:j+k+1])) in flowers[j:j+k+1]:
				result+=1
		
	print(result)

if __name__ == "__main__":
	solver()