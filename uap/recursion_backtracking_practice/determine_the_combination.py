from sys import stdin
from itertools import combinations

def combine(s, start, r, end):
    pass

for line in stdin:
    s, r = line.split()
    r = int(r)
    s = list(s)
    s.sort()
    s = sorted(list(set(combinations(s, r))))
    
    for per in s:
        print("".join(per))