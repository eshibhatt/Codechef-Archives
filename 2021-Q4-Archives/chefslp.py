T= int(input())

for i in range(0,T):
    N,L,X=map(int,input().split())
    R=N-L
    if R>L:
        p= X*L
    elif L>R:
        p= X*R
    elif R==L:
        p=X*R
    print(p)
