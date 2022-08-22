for _ in range(int(input())):
    N=int(input())
    S=input()
    count=0
    i=0
    while i<len(S):
        if i==len(S)-1:
            count+=1
            break
        if S[i]==S[i+1]:
            count+=1
            i+=2
        else:
            count+=1
            i+=1
    print(count)