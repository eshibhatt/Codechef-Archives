T=int(input())
def get_divisors(n) :
    i=1
    L=[]
    while i<=n:
        if (n%i==0):
            L.append(i)
        i = i + 1
    return L
def isprime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True
for i in range(0,T):
    N=int(input())
    count=0
    for i in range(0,N):
        a=get_divisors(i)
        b=len(a)
        if b%2!=0 and isprime(b) is True:
            count+=1
    print(count)
