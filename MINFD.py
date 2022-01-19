for i in range(int(input())):
    N,X=map(int,input().split())
    arr=input().split()

    acc=0
    count=0

    for j in range(0,len(arr)):
        if acc<X:
            c=int(arr[j])
            acc+=c
        elif acc>=X:
            ind=j
            break
    
    if acc<X:
        print('-1')
    elif acc>=X:
        print(ind)