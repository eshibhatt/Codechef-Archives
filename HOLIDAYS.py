for i in range(int(input())):
    N,W=map(int,input().split())
    Arr=[int(i) for i in input().split()]
    ac=0
    while ac<W:
        add=max(Arr)
        ac+=add
        Arr.remove(add)
    
    hol=len(Arr)
    print(hol)