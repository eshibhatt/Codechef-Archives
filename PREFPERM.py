t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=[int(i) for i in input().split()]
    ans=[]
    prev=0
    for i in range(0,k):
        val=arr[i]
        while val>prev:
            ans.append(val)
            val-= 1
        prev=arr[i]
    for j in ans:
        print(j, end=" ")
    print()