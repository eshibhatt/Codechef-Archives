def maxHoliday(S):
    count=0
    maxTillNow=0
    k=0
    while k<len(S):
        if S[k]=='0':
            count+=1
            if S[k-1]!='0':
                start=k
        if count>maxTillNow:
            maxTillNow=count
        elif S[k]==1:
            end=k
            count=0
    return maxTillNow,start,end

for i in range(int(input())):
    N,X=map(int,input().split())
    S=input().split()

    holidayMax,start,end=maxHoliday(S)
    
    S2=S
    S2[start]='0'
    holidayMax2,start2,end2=maxHoliday(S2)

    S3=S
    S3[end]='0'
    holidayMax3,start3,end3=maxHoliday(S3)

    if holidayMax2>=holidayMax3:
        vaction=holidayMax2/X
    else:
        vaction=holidayMax3/X
    
    print(vaction)