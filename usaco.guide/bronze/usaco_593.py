import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	farm = [[0]*(100*10*2+1) for i in range((100*10*2+1))]
	t = 0
	lr = 1000
	ud = 1000
	result = float('inf')
	for i in range(int(input())):
		d, s = input().split()
		for j in range(int(s)):
			t+=1
			if d=='N':
				ud-=1
			elif d=='S':
				ud+=1
			elif d=='E':
				lr+=1
			elif d=='W':
				lr-=1
			
			if farm[ud][lr]:
				result = min(t-farm[ud][lr],result)

			farm[ud][lr] = t
	if result==float("inf"):
		print(-1)
		return
	print(result)
if __name__ == "__main__":
	solver('mowing')