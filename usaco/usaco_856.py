def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    n = int(input())
    buckets = [0]*1001
    for i in range(n):
        s,t,b = map(int,input().split())
        for j in range(s,t+1):
            buckets[j]+=b
    
    print(max(buckets))

if __name__ == "__main__":
	solver('blist')