t=int(input())
for i in range(0,t):
    N=int(input())
    S=input()
    lst=[]
    for k in range(0,len(S)):
        lst.append(S[k])
    
    oneCount=lst.count('1')
    zeroCount=lst.count('0')
    qCount=lst.count('?')

    stri=[]
    for j in range(0,qCount):
        if oneCount>zeroCount:
            stri.append('0')
            zeroCount+=1
            continue
        elif oneCount<zeroCount:
            stri.append('1')
            oneCount+=1
            continue
        else:
            stri.append('0')
            zeroCount+=1
    s=0
    for l in range(0,len(lst)-1):
        if lst[l]=='?':
            lst[l]=stri[s]
            s+=1
         
    print(''.join(lst))
