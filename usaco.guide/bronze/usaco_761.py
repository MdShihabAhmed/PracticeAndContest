import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	cows = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
	days = [0]*(100+1)
	for i in range(int(input())):
		day, name, change = input().split()
		days[int(day)] = (name, change)
	
	result = 0
	previous = ('Bessie', 'Elsie', 'Mildred')
	for i in range(100+1):
		if not days[i]:
			continue
		
		cows[days[i][0]]+=int(days[i][1])
		
		m = max(cows.values())
		current = (k for k,v in cows.items() if cows[k]==m)
		if previous != current:
			result +=1
		previous = current
	
	print(result)
if __name__ == "__main__":
	solver('measurement')