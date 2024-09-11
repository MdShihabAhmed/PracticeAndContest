#unsolved yet: skipped for now
import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	start = [0, float("inf")]
	end = [0, float("inf")]
	on = [0, 0]
	off = [0, 0]
	none = [0, float("inf")]
	for _ in range(int(input())):
		s, seg = input().split()
		l, r = map(int,seg)
		if s=='on':
			on[0] += l
			on[1] += r
		elif s=='off':
			off[0] += l
			off[1] += r
		else:
			none = [max(none[0],l), min(none[1],r)]
			
			start[0] = none[0]-on[1]
			start[1] = none[1]-on[0]
			on = [0, 0]

			end[0] = none[0]-off[1]
			end[1] = none[1]-off[0]
			off = [0, 0]
	print(start[0],start[1])
	print(end[0],end[1])

if __name__ == "__main__":
	solver('traffic')