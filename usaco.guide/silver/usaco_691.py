import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n = int(input())

	h = [0]
	p = [0]
	s = [0]

	for i in range(n):
		c = input().rstrip()
		h.append(h[-1])
		p.append(p[-1])
		s.append(s[-1])

		if c=='H':
			h[-1]+=1
		elif c=='P':
			p[-1]+=1
		elif c=='S':
			s[-1]+=1
	
	result = 0
	for i in range(n+1):
		result = max(result,max(h[i],p[i],s[i])+max(h[n]-h[i],p[n]-p[i],s[n]-s[i]))
	
	print(result)


if __name__ == "__main__":
	solver('hps')