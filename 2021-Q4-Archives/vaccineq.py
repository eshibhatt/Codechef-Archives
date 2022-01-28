T=int(input())

for i in range(0,T):
    time=0
    N,P,X,Y=map(int,input().split())
    K=input().split()
    if P==0:
        time=Y
        print(time)
        continue
    else:
        for a in K[0:P]:
            if a=='0':
                time+=X
            elif a=='1':
                time+=Y
        print(time)