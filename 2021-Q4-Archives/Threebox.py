T= int(input())

for i in range(0,T):
    A,B,C,D=map(int,input().split())
    count=0
    if A+B+C<=D:
        count+=1
        print(count)
        continue
    if A+B<=D:
        count+=1
        if C==0:
            print(count)
        else:
            count+=1
            print(count)
    elif B+C<=D:
        count+=1
        if A==0:
            print(count)
        else:
            count+=1
            print(count)
    elif C+A<=D:
        count+=1
        if B==0:
            print(count)
        else:
            count+=1
            print(count)
    else:
        count+=3
        print(count)
