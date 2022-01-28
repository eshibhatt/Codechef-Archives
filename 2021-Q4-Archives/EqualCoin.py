T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    onecoin=X*1
    twocoin=Y*2
    Z=onecoin+twocoin
    if Z%2==0:
        print("YES")
    else:
        print("NO")