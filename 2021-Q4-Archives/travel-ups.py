T=int(input())

for i in range(0,T):
    N,A,B=map(int,input().split())
    S=list(input())
    count=0        #increments on each iteration
    for j in S:
        if j=='0':  #as the integer is in a string, it can be compared to a string only
            count+=A
        if j=='1':
            count+=B
    print(count)