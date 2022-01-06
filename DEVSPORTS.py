T= int(input())

for i in range(0,T):
  z,y,a,b,c=map(int,input().split())
  available=z-y
  reqd=a+b+c

  if available>reqd or available==reqd:
    print('YES')
  else:
    print('NO')