T=int(input())

for i in range(0,T):
  X,Y,P,Q = map(int,input().split())

  chefPen=(P*10)+X
  chefiP=(Q*10)+Y

  if chefPen>chefiP:
    print('Chefina')
  elif chefPen<chefiP:
    print('Chef')
  else:
    print('Draw')
    

  
