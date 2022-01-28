#Generate a no of N digits, divisible by 3 but not 9 and odd.

T= int(input())

for i in range(0,T):
    N=int(input())
    L=10**(N-1) #lower limit of digit range
    U=(10**N)-1 #upper limit of digit range
    for j in range(L,U):
        if j%3==0 and j%9!=0 and j%2!=0:
            print(j)
            break