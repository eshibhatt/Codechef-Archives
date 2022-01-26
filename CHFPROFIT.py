for i in range(int(input())):
    x,y,z=map(int,input().split())

    bought=x*y
    sold=x*z

    profit= sold-bought

    print(profit)