import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, l, r = map(int,input().split())
    a = list(map(int,input().split()))
    part1 = a[:l-1]
    part2 = a[l-1:r]
    part3 = a[r:]
    part1.sort()
    part2.sort()
    part3.sort()
    s1 = 0
    s21 = sum(part2)
    s22 = s21
    s23 = s21
    s3 = 0

    for i in range(min(len(part1),r-l+1)):
        s1+=min(part1[i],part2[r-l-i])
        s21-=part2[r-l-i]

    for i in range(min(len(part3),r-l+1)):
        s3+=min(part3[i],part2[r-l-i])
        s22-=part2[r-l-i]

    print(min(s21+s1,s22+s3,s23))
