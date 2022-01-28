# cook your dish here
T=int(input())

for i in range(0,T):
    count=0
    fstyp=0
    scndtyp=0
    N,A,B,C=map(int,input().split())
    while A>=1 and B>=1:
        fstyp+=1
        A-=1
        B-=1
    while B>=1 and C>=1:
        scndtyp+=1
        C-=1
        B-=1
    if fstyp + scndtyp >=N:
        print('YES')
    else:
        print('NO')
