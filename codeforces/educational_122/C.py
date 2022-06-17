def solver(hc,dc,hm,dm,k,w,a):
    attacksForMonster= hc//dm
    if hc%dm:
        attacksForMonster+=1
    
    attacksForCharacter = hm//dc
    if hm%dc:
        attacksForCharacter+=1

    if attacksForCharacter<=attacksForMonster:
        return 'YES'
    
    for i in range(0,k+1):
        attacksForMonster= (hc+a*i)//dm
        if (hc+a*i)%dm:
            attacksForMonster+=1
        
        attacksForCharacter = hm//(dc+w*(k-i))
        if hm%(dc+w*(k-i)):
            attacksForCharacter+=1

        if attacksForCharacter<=attacksForMonster:
            return 'YES'

    return 'NO'


t = int(input())

for _ in range(t):
    hc,dc = map(int, input().split())
    hm,dm = map(int, input().split())
    k,w,a = map(int, input().split())

    print(solver(hc,dc,hm,dm,k,w,a))