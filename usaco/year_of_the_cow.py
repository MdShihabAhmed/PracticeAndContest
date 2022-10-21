from collections import defaultdict
import sys

input = sys.stdin.readline
cycle = 'Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat'.split(', ')
year = {cycle[i]: i+1 for i in range(12)}
cows = {'Bessie':'Ox'}
distance = defaultdict(int)
def solve(cow,cow2, first, condition, last):
    temp = 0
    if condition=='next':
        temp=first-last
        if first<=last:
            temp+=12
    else:
        temp = last-first
        if last<=first:
            temp+=12
        temp*=-1
    # print(cow, temp)
    distance[cow] = distance[cow2]+temp

stop = ''
result = 0
for i in range(int(input())):
    s = input().rstrip().split()
    cows[s[0]] = s[4]
    if stop=='Elsie':
        continue
    # print(cows[s[0]],s[3],cows[s[-1]])
    solve(s[0],s[-1],year[cows[s[0]]],s[3],year[cows[s[-1]]])
    if s[0]=='Elsie':
        stop = 'Elsie'
print(abs(distance['Elsie']))