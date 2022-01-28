T= int(input())

for i in range(0,T):
    X,Y,A,B,K=map(int,input().split())
    count=0
    while count<=K:
        X=X+A
        Y=Y+B
        count+=1
    if X<Y:
        print("PETROL")
    elif X==Y:
        print('SAME PRICE')
    else:
        print("DIESEL")
