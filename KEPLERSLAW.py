T=int(input())

for i in range(0,T):
  t1,t2,r1,r2=map(int,input().split())

  #checking if the proportionality constants of each case are equal
  if (t1**2)/(r1**3)==(t2**2)/(r2**3):
    print("Yes")
  else:
    print("No")
