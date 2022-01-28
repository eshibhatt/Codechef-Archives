T=int(input())
for i in range(0,T):
    a,b=map(int,input().split())
    c=a+b
    if c%2==0:
        print('Bob')
    else:
        print('Alice')