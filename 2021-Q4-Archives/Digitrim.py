#least no to be added to an integer such that it does not contain the input digit

T=int(input())

for i in range(0,T):
    N,D=map(int,input().split())
    lst=[int(x) for x in str(N)] #list which contains all digits in N
    add=0
    while lst.count(D)!=0:
        N+=1
        add+=1
        lst=[int(x) for x in str(N)]
    print(add)
