for _ in range(int(input())):
    N=int(input())
    
    c=N*10
    rem=c%9
    req=0

    if rem!=0:
        req=9-rem
        c+=req
    
    print(c)