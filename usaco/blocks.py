from collections import Counter

def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')


    n = int(input())
    letter = [0]*26
    for i in range(n):
        side1, side2 = input().split()
        side1 = Counter(side1)
        side2 = Counter(side2)
        both = dict(side1)
        
        for key, value in side2.items():
            if key in both:
                both[key] = max(value,both[key])
            else:
                both[key] = value

        for key, value in both.items():
            letter[ord(key)-97]+=value
    
    print('\n'.join([str(i) for i in letter]))
    


if __name__ == "__main__":
	solver('blocks')