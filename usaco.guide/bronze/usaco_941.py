import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	n = int(input())
	level = dict()
	population = []

	for i in range(n):
		temp = list(input().split())
		k = int(temp[0])
		population.append(temp[1:])
		for feature in population[-1]:
			if feature in level:
				level[feature] = min(k,level[feature])
			else:
				level[feature] = k

	for sub in population:
		cnt = 0
		temp = [100]
		for i in range(len(sub)):
			temp.append(level[sub[i]])
		mini = min(temp)

		for i in temp:
			if mini==i:
				cnt+=1
		if mini-cnt<0:
			print('no')
			break
	else:
		print('yes')

if __name__ == "__main__":
	solver('evolution')