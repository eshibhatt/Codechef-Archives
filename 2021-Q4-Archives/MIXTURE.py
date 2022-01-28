T= int(input())

for i in range(0,T):
    A,B=map(int,input().split())

    if A>0 and B>0:
        print('Solution')
    elif B==0:
        print('Solid')
    elif A==0:
        print('Liquid')
