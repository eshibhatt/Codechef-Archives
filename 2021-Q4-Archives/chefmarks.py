X=int(input())
Y=int(input())
Z=int(input())

if X>=Y and X>=Z:
    if Y>=Z:
        print(Y)
    else:
        print(Z)
elif Y>=X and Y>=Z:
    if X>=Z:
        print(X)
    else:
        print(Z)
elif Z>=X and Z>=Y:
    if X>=Y:
        print(X)
    else:
        print(Y)
