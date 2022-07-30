from itertools import permutations
s = input()
per = list(map("".join, permutations(s)))

per.sort()
result = []
temp = -1

for i in per:
    if i==temp:
        continue
    temp = i
    result.append(temp)
 
print(len(result))
print('\n'.join(result))