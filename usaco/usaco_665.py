input = open('cowsignal.in', 'r').readline
fout = open('cowsignal.out', 'w')
print = lambda x: fout.write(str(x)+'\n')

m, n, k = map(int,input().split())
for _ in range(m):
    s = input().rstrip()
    result = ''
    for c in s:
        result+=(c*k)
    for i in range(k):
        print(f'{result}')