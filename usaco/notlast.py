import sys


def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

    milking = {cow: 0 for cow in cows}

    for i in range(int(input())):
        cow, milk = input().split()
        milking[cow]+=int(milk)
    
    firstMin = secondMin = 10**5
    values = set()
    for key,value in milking.items():
        values.add(value)
    
    values = sorted(list(values))
    if len(values)<2:
        print('Tie')
    else:
        count = 0
        cow = ''
        for key,value in milking.items():
            if value==values[1]:
                cow = key
                count+=1
        if count>1:
            print('Tie')
        else:
            print(cow)

if __name__ == "__main__":
	solver('notlast')