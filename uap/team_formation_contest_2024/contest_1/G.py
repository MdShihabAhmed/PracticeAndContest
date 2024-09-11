students = []

n = int(input())

for i in range(n):
    temp = input().split()
    students.append([temp[0]]+list(map(int,temp[1:])))
students.sort(key= lambda x:[-x[4],-x[2],-x[1],-x[3],x[0]])
for i in students:
    print(i[0])