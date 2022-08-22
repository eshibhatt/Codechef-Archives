for i in range(int(input())):
    # X,A,B=map(int,input().split())
    N=int(input())
    # Arr=[int(x) for x in input ().split()]
    Arr=list(map(int,input().split()))
    count=0
    
    for j in range(0,len(Arr)):
        if Arr[j]>=10 and Arr[j]<=60:
            count+=1
        else:
            continue
    print(count)