T=int(input())

for i in range(0,T):
  N,D=map(int,input().split())
  infected=1
  
  for i in range(1,D+1):
    if i<=10:
      infected=infected*2
    else:
      infected=infected*3

    if infected>=N:
      infected=N
      break

  print(infected)
